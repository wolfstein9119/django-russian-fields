from django.contrib import admin
from .models import SampleModel


class SampleModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'gender', 'agency_type_esia', 'territory_code'
    )


admin.site.register(SampleModel, SampleModelAdmin)
