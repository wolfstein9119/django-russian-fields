from django.db import models
from django.core.validators import MinLengthValidator, BaseValidator
from django.core import checks
from .validators import (
    ProbablyLengthValidator, IsDigitValidator, ControlNumberValidation
)
from .meta_info import OGRNMeta


class OGRN(str):
    def detect_mode(self):
        l = len(self)
        if l == OGRNMeta.BUSINESS_ORGN_LENGTH:
            return OGRNMeta.BUSINESS_MODE
        elif l == OGRNMeta.LEGAL_OGRN_LENGTH:
            return OGRNMeta.LEGAL_MODE
        return None

    @property
    def feature(self):
        return self[:1]

    @property
    def year(self):
        return self[1:3]

    @property
    def region_code(self):
        return self[3:5]

    @property
    def inspection_code(self):
        return self[5:7]

    @property
    def record_number(self):
        start_index, end_index = OGRNMeta.get_range(self.detect_mode(), 'record_number_range')
        return self[start_index:end_index]

    @property
    def control_number(self):
        start_index, end_index = OGRNMeta.get_range(self.detect_mode(), 'control_number_range')
        return self[start_index:end_index]

    @property
    def is_valid_control(self):
        mode = self.detect_mode()
        if self.isdigit():
            if mode == OGRNMeta.LEGAL_MODE:
                return self._check_legal()
            elif mode == OGRNMeta.BUSINESS_MODE:
                return self._check_business()
        return False

    def _check_legal(self):
        control_number, tested_number = self._get_control_operand()
        return tested_number % 11 % 10 == control_number

    def _check_business(self):
        control_number, tested_number = self._get_control_operand()
        return tested_number % 13 == control_number

    def _get_control_operand(self):
        control_number = int(self.control_number)
        start_index, end_index = OGRNMeta.get_range(self.detect_mode(), 'without_control_range')
        tested_number = int(self[start_index: end_index])
        return control_number, tested_number


class OGRNField(models.CharField):
    # legal - ЮЛ
    # business - ИП
    # general - общий ОГРН

    description = 'OGRN (legal / business / general)'

    def __init__(self, *args, **kwargs):
        self.mode = kwargs.pop('mode', OGRNMeta.GENERAL_MODE)
        min_length, max_length = OGRNMeta.get_length(self.mode)
        kwargs['max_length'] = max_length
        super(OGRNField, self).__init__(*args, **kwargs)
        self.validators.extend([
            MinLengthValidator(min_length),
            ProbablyLengthValidator(OGRNMeta.available_length),
            IsDigitValidator(),
            ControlNumberValidation()
        ])

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return OGRN(value)

    def to_python(self, value):
        if isinstance(value, OGRN):
            return value
        if value is None:
            return value
        return OGRN(value)

    def check(self, **kwargs):
        errors = super(OGRNField, self).check(**kwargs)
        errors.extend(self._check_ogrn_settings())
        return errors

    def _check_ogrn_settings(self):
        if self.mode not in OGRNMeta.available_mode:
            return [
                checks.Error(
                    "OGRNFields must define a valid 'mode' attribute. %s" % self.available_mode,
                    obj=self
                )
            ]
        else:
            return []

    def deconstruct(self):
        name, path, args, kwargs = super(OGRNField, self).deconstruct()
        del kwargs['max_length']
        if self.mode != OGRNMeta.GENERAL_MODE:
            kwargs['mode'] = self.mode
        return name, path, args, kwargs


class OGRNBusinessField(OGRNField):
    def __init__(self, *args, **kwargs):
        kwargs['mode'] = OGRNMeta.BUSINESS_MODE
        super(OGRNBusinessField, self).__init__(*args, **kwargs)


class OGRNLegalField(OGRNField):
    def __init__(self, *args, **kwargs):
        kwargs['mode'] = OGRNMeta.LEGAL_MODE
        super(OGRNLegalField, self).__init__(*args, **kwargs)
