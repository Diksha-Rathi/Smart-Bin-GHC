from django.contrib import admin
from bins.models import *

class Display_Definition(admin.ModelAdmin):
    list_display = ('location_id', 'bin_id', 'fill_level', 'humidity', 'temperature')

# Register your models here.
admin.site.register(bin_info, Display_Definition)