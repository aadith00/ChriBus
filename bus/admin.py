from django.contrib import admin
from .models import Bus, Booking

class BusAdmin(admin.ModelAdmin):
    list_display = ('num_plate', 'driver_id', 'departure_date', 'total_seats')
    search_fields = ('num_plate', 'driver_id', 'departure_date')

admin.site.register(Bus, BusAdmin)


admin.site.register(Booking)
