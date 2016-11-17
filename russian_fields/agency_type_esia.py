from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy as _


class AgencyTypeESIA(models.CharField):
    description = _("AgencyTypeESIA")
    DEFAULT_MAX_LENGTH = DEFAULT_MIN_LENGTH = 6

    FEDERAL_EXECUTIVE = '10.FED'
    STATE_OFF_BUDGET_FOND = '30.FND'
    TERRITORY_EXECUTIVE = '11.REG'
    LOCAL_AUTHORITY = '12.LCL'
    GOVERNMENT_INSTITUTION = '20.GOV'
    MUNICIPAL_INSTITUTION = '21.MCL'

    TYPE_CHOICE = (
        (FEDERAL_EXECUTIVE, _('The federal executive government')),
        (STATE_OFF_BUDGET_FOND, _('State off-budget fund')),
        (TERRITORY_EXECUTIVE, _('The territory executive government')),
        (LOCAL_AUTHORITY, _('Local authority')),
        (GOVERNMENT_INSTITUTION, _('Government institution')),
        (MUNICIPAL_INSTITUTION, _('Municipal institution')),
    )

    def __init__(self, *args, **kwargs):
        max_length = self.DEFAULT_MAX_LENGTH
        min_length = self.DEFAULT_MIN_LENGTH
        kwargs['max_length'] = max_length
        kwargs['choices'] = self.TYPE_CHOICE
        super(AgencyTypeESIA, self).__init__(*args, **kwargs)
        self.validators.extend([
            MinLengthValidator(min_length),
        ])

    def deconstruct(self):
        name, path, args, kwargs = super(AgencyTypeESIA, self).deconstruct()
        del kwargs['max_length']
        del kwargs['choices']
        return name, path, args, kwargs
