from django.contrib import admin
from .models import SampleModel


class SampleModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'gender'
    )


admin.site.register(SampleModel, SampleModelAdmin)
