from django.core.validators import BaseValidator
from django.utils.translation import ugettext_lazy as _


class ProbablyLengthValidator(BaseValidator):
    message = _('Ensure this value has at %(limit_value)s characters (it has %(show_value)d).')
    code = 'probably_length'

    def compare(self, a, b):
        return a not in b

    def clean(self, x):
        return len(x)


class IsDigitValidator(BaseValidator):
    message = _('Ensure this value has only digit characters.')
    code = 'id_digit'

    def __init__(self, limit_value=None, message=None):
        super(IsDigitValidator, self).__init__(limit_value, message)

    def compare(self, a, b):
        return not a.isdigit()
