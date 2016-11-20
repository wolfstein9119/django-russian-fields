from django.db import models
from django.core.validators import MinLengthValidator
from .validators import IsDigitValidator


class OKOGUField(models.CharField):
    # Общероссийский классификатор органов гос.власти
    description = 'OKOGU'
    DEFAULT_MAX_LENGTH = DEFAULT_MIN_LENGTH = 7

    def __init__(self, *args, **kwargs):
        max_length = self.DEFAULT_MAX_LENGTH
        min_length = self.DEFAULT_MIN_LENGTH
        kwargs['max_length'] = max_length
        super(OKOGUField, self).__init__(*args, **kwargs)
        self.validators.extend([
            MinLengthValidator(min_length),
            IsDigitValidator()
        ])

    def deconstruct(self):
        name, path, args, kwargs = super(OKOGUField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs
