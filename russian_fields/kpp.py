from django.db import models
from django.core.validators import MinLengthValidator


class KPP(str):
    @property
    def inspection_code(self):
        return self[:4]

    @property
    def cause(self):
        return self[4:6]

    @property
    def record_number(self):
        return self[6:9]


class KPPField(models.CharField):
    description = 'KPP'
    DEFAULT_MAX_LENGTH = DEFAULT_MIN_LENGTH = 9

    def __init__(self, *args, **kwargs):
        max_length = self.DEFAULT_MIN_LENGTH
        min_length = self.DEFAULT_MIN_LENGTH
        kwargs['max_length'] = max_length
        super(KPPField, self).__init__(*args, **kwargs)
        self.validators.extend([
            MinLengthValidator(min_length),
        ])

    def deconstruct(self):
        name, path, args, kwargs = super(KPPField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return KPP(value)

    def to_python(self, value):
        if isinstance(value, KPP):
            return value
        if value is None:
            return value
        return KPP(value)
