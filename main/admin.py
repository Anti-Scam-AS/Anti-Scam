from django.contrib import admin

# Register your models here.

from .models import Vacant, Vacant_report

admin.site.register(Vacant)
admin.site.register(Vacant_report)