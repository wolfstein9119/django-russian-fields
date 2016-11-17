from django.db import models
from russian_fields import (
    GENDERField, AgencyTypeESIA, TerritoryCodeField
)


class SampleModel(models.Model):
    gender = GENDERField(
        blank=True, null=True
    )
    agency_type_esia = AgencyTypeESIA(
        blank=True, null=True
    )
    territory_code = TerritoryCodeField(
        blank=True, null=True
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'SampleModel'
        verbose_name_plural = 'SampleModels'
