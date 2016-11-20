from django.db import models
from russian_fields import (
    GENDERField, AgencyTypeESIA, TerritoryCodeField,
    INNField, INNPersonField, INNBusinessField, KPPField,
    OGRNField, OGRNBusinessField, OGRNLegalField,
    OKOGUField, OKOPFField
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


class Sample2Model(models.Model):
    inn = INNField(
        blank=True, null=True
    )
    inn_person = INNPersonField(
        blank=True, null=True
    )
    inn_business = INNBusinessField(
        blank=True, null=True
    )
    kpp = KPPField(
        blank=True, null=True
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Sample2Model'
        verbose_name_plural = 'Sample2Models'


class Sample3Model(models.Model):
    ogrn = OGRNField(
        blank=True, null=True
    )
    ogrn_legal = OGRNLegalField(
        blank=True, null=True
    )
    ogrn_business = OGRNBusinessField(
        blank=True, null=True
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Sample3Model'
        verbose_name_plural = 'Sample3Models'


class Sample4Model(models.Model):
    okogu = OKOGUField(
        blank=True, null=True
    )
    okopf = OKOPFField(
        blank=True, null=True
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Sample4Model'
        verbose_name_plural = 'Sample4Models'
