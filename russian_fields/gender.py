from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy as _


class GENDERField(models.CharField):
    description = _("GENDER")
    DEFAULT_MAX_LENGTH = DEFAULT_MIN_LENGTH = 1
    DEFAULT_MEMBER_NAME = 'gender'

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, _("Male")),
        (GENDER_MALE, _("Female")),
    )

    def __init__(self, *args, **kwargs):
        max_length = self.DEFAULT_MAX_LENGTH
        min_length = self.DEFAULT_MIN_LENGTH
        kwargs['max_length'] = max_length
        kwargs['choices'] = self.GENDER_CHOICES
        super(GENDERField, self).__init__(*args, **kwargs)
        self.validators.extend([
            MinLengthValidator(min_length),
        ])

    def deconstruct(self):
        name, path, args, kwargs = super(GENDERField, self).deconstruct()
        del kwargs['max_length']
        del kwargs['choices']
        return name, path, args, kwargs
