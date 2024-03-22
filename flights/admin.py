from django.contrib import admin
from .models import Airport, Flight, Passenger

# Register your models here.
class flightAdmin(admin.ModelAdmin):
    list_display = ("id","origin", "destination", "duration", )

class passengerAdmin(admin.ModelAdmin):
    filter_vertical = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, flightAdmin)
admin.site.register(Passenger, passengerAdmin)