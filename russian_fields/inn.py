from django.db import models
from django.core import checks
from django.core.validators import MinLengthValidator
from .validators import (
    ProbablyLengthValidator, IsDigitValidator, ControlNumberValidation
)
from .meta import INNMeta


class INN(str):
    def detect_mode(self):
        l = len(self)
        if l == INNMeta.PERSON_INN_LENGTH:
            return INNMeta.PERSON_MODE
        elif l == INNMeta.LEGAL_INN_LENGTH:
            return INNMeta.LEGAL_MODE
        return None

    @property
    def region_code(self):
        return self[:2]

    @property
    def inspection_code(self):
        return self[2:4]

    @property
    def record_number(self):
        start_index, end_index = INNMeta.get_range(self.detect_mode(), 'control_number_range')
        return self[start_index:end_index]

    @property
    def control_number(self):
        start_index, end_index = INNMeta.get_range(self.detect_mode(), 'control_number_range')
        return self[start_index:end_index]

    @property
    def is_valid_control(self):
        mode = self.detect_mode()
        if self.isdigit():
            if mode == INNMeta.LEGAL_MODE:
                return self._check_legal()
            elif mode == INNMeta.PERSON_MODE:
                return self._check_person()
        return False

    def _check_legal(self):
        control_number = int(self.control_number)
        n1, n2, n3, n4, n5, n6, n7, n8, n9 = map(lambda u: int(u), self[:-1])
        return (
                   2 * n1 + 4 * n2 + 10 * n3 + 3 * n4 + 5 * n5 + 9 * n6 + 4 * n7 + 6 * n8 + 8 * n9
               ) % 11 % 10 == control_number

    def _check_person(self):
        control_number = int(self.control_number)
        control_number_1 = int(control_number / 10)
        control_number_2 = control_number % 10
        n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = map(lambda u: int(u), self[:-1])
        exp_1 = (
                    7 * n1 + 2 * n2 + 4 * n3 + 10 * n4 + 3 * n5 + 5 * n6 + 9 * n7 + 4 * n8 + 6 * n9 + 8 * n10
                ) % 11 % 10 == control_number_1
        exp_2 = (
                    3 * n1 + 7 * n2 + 2 * n3 + 4 * n4 + 10 * n5 + 3 * n6 + 5 * n7 + 9 * n8 + 4 * n9 + 6 * n10 + 8 * n11
                ) % 11 % 10 == control_number_2
        return exp_1 and exp_2


class INNField(models.CharField):
    # person - физ. ИНН
    # legal - юр. ИНН
    # general - общий ИНН

    description = 'INN (person / legal / general)'

    def __init__(self, *args, **kwargs):
        self.mode = kwargs.pop('mode', INNMeta.GENERAL_MODE)
        min_length, max_length = INNMeta.get_length(self.mode)
        kwargs['max_length'] = max_length
        super(INNField, self).__init__(*args, **kwargs)
        self.validators.extend([
            MinLengthValidator(min_length),
            ProbablyLengthValidator(INNMeta.available_length),
            IsDigitValidator(),
            ControlNumberValidation()
        ])

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return INN(value)

    def to_python(self, value):
        if isinstance(value, INN):
            return value
        if value is None:
            return value
        return INN(value)

    def check(self, **kwargs):
        errors = super(INNField, self).check(**kwargs)
        errors.extend(self._check_inn_settings())
        return errors

    def _check_inn_settings(self):
        if self.mode not in INNMeta.available_mode:
            return [
                checks.Error(
                    "INNFields must define a valid 'mode' attribute. %s" % self.available_mode,
                    obj=self
                )
            ]
        else:
            return []

    def deconstruct(self):
        name, path, args, kwargs = super(INNField, self).deconstruct()
        del kwargs['max_length']
        if self.mode != INNMeta.GENERAL_MODE:
            kwargs['mode'] = self.mode
        return name, path, args, kwargs


class INNPersonField(INNField):
    def __init__(self, *args, **kwargs):
        kwargs['mode'] = INNMeta.PERSON_MODE
        super(INNPersonField, self).__init__(*args, **kwargs)


class INNBusinessField(INNField):
    def __init__(self, *args, **kwargs):
        kwargs['mode'] = INNMeta.LEGAL_MODE
        super(INNBusinessField, self).__init__(*args, **kwargs)
