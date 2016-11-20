from django.db import models
from django.core.validators import MinLengthValidator
from .validators import IsDigitValidator


class OKOPFField(models.CharField):
    # Общероссийский классификатор организационной-правовых форм
    description = 'OKOPF'
    DEFAULT_MAX_LENGTH = DEFAULT_MIN_LENGTH = 5

    def __init__(self, *args, **kwargs):
        max_length = self.DEFAULT_MAX_LENGTH
        min_length = self.DEFAULT_MIN_LENGTH
        kwargs['max_length'] = max_length
        super(OKOPFField, self).__init__(*args, **kwargs)
        self.validators.extend([
            MinLengthValidator(min_length),
            IsDigitValidator()
        ])

    def deconstruct(self):
        name, path, args, kwargs = super(OKOPFField, self).deconstruct()
        del kwargs['max_length']
        return name, path, args, kwargs
