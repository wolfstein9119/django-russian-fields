from django.contrib import admin
from .models import SampleModel, Sample2Model


class SampleModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'gender', 'agency_type_esia', 'territory_code'
    )


class Sample2ModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'inn', 'inn_person', 'inn_business', 'kpp'
    )


admin.site.register(SampleModel, SampleModelAdmin)
admin.site.register(Sample2Model, Sample2ModelAdmin)
