from django.db import models
from django.core.validators import MinLengthValidator
from .validators import IsDigitValidator


class TerritoryCodeField(models.CharField):
    # код субъекта РФ
    description = 'Territory code'
    DEFAULT_MAX_LENGTH = DEFAULT_MIN_LENGTH = 2

    def __init__(self, *args, **kwargs):
        max_length = self.DEFAULT_MAX_LENGTH
        min_length = self.DEFAULT_MIN_LENGTH
        kwargs['max_length'] = max_length
        super(TerritoryCodeField, self).__init__(*args, **kwargs)
        self.validators.extend([
            MinLengthValidator(min_length),
            IsDigitValidator()
        ])

    def deconstruct(self):
        name, path, args, kwargs = super(TerritoryCodeField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs
