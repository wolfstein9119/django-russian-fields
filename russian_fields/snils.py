from functools import reduce

from django.db import models
from django.core.validators import MinLengthValidator
from .validators import (
    IsDigitValidator, ControlNumberValidation
)


class SNILS(str):
    RAZOR = '001-001-998'
    control_mask = range(9, 0, -1)

    @property
    def representation(self):
        return '%s-%s-%s %s' % (
            self[0:3], self[3:6], self[6:9], self[9:11]
        )

    @property
    def record_number(self):
        return self[0:9]

    @property
    def control_number(self):
        return int(self[9:11])

    @property
    def is_valid_control(self):
        if self <= self.RAZOR:
            return ValueError('Unverifiable SNILS')
        return self._check_control_number()

    def _check_control_number(self):
        summ = self._get_position_sum()
        if summ > 101:
            summ %= 101
        return self._check_position_summ(summ)

    def _check_position_summ(self, summ):
        if summ < 100:
            return summ == self.control_number
        if summ in (100, 101):
            return self.control_number == 0
        return False

    def _get_position_sum(self):
        def pair_processor(s, p):
            s, p = int(s), int(p)
            return s*p

        pos_control = [pair_processor(s, p) for s, p in zip(self.record_number, self.control_mask)]
        summ = reduce(lambda res, x: res + x, pos_control, 0)
        return summ


class SNILSField(models.CharField):
    description = 'SNILS'
    DEFAULT_MAX_LENGTH = DEFAULT_MIN_LENGTH = 11
    STOP_CHARACTER = '- _'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = self.DEFAULT_MAX_LENGTH
        super(SNILSField, self).__init__(*args, **kwargs)
        self.validators.extend([
            MinLengthValidator(self.DEFAULT_MIN_LENGTH),
            IsDigitValidator(),
            ControlNumberValidation()
        ])

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return SNILS(value)

    def to_python(self, value):
        if isinstance(value, SNILS):
            return value
        if value is None:
            return value
        return SNILS(value)

    def deconstruct(self):
        name, path, args, kwargs = super(SNILSField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if value:
            value = reduce(
                lambda res, x: res.replace(x, ''),
                self.STOP_CHARACTER,
                value
            )
            setattr(model_instance, self.attname, value)
        return value
