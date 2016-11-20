from django.contrib import admin
from .models import (
    SampleModel, Sample2Model, Sample3Model, Sample4Model
)


class SampleModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'gender', 'agency_type_esia', 'territory_code'
    )


class Sample2ModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'inn', 'inn_person', 'inn_business', 'kpp'
    )


class Sample3ModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'ogrn', 'ogrn_legal', 'ogrn_business'
    )


class Sample4ModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'okogu', 'okopf'
    )


admin.site.register(SampleModel, SampleModelAdmin)
admin.site.register(Sample2Model, Sample2ModelAdmin)
admin.site.register(Sample3Model, Sample3ModelAdmin)
admin.site.register(Sample4Model, Sample4ModelAdmin)
