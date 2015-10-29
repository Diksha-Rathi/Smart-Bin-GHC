from django.contrib import admin
from bins.models import *


class Display_Definition1(admin.ModelAdmin):
	  list_display = ('location_id', 'longitude', 'latitude')

class Display_Definition2(admin.ModelAdmin):
	  list_display = ('location_id', 'bin_id', 'date', 'fill_level', 'humidity', 'temperature')

# Register your models here.
admin.site.register(bin_record, Display_Definition1)
admin.site.register(bin_updates, Display_Definition2)


# from django.contrib import admin
# from binDetails.models import *
# # Register your models here.
# admin.site.register(binAdded)
# admin.site.register(binDescription)