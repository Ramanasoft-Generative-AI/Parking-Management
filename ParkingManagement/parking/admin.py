from django.contrib import admin
from .models import Category
from .models import AddVehicle

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parking_area_no', 'vehicle_type', 'vehicle_limit', 'parking_charge',
                    'status', 'doc', 'action')
    list_editable = ('status', 'action')
    search_fields = ('id', 'parking_area_no', 'vehicle_type', 'vehicle_limit', 'parking_charge',
                    'status', 'doc', 'action')
    list_display_links = ('vehicle_type',)
    ordering = ('id',)


class AddVehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'parking_area_no', 'vehicle_type', 'parking_charge',
                    'status', 'arrival_time', 'action')
    list_editable = ('status', 'action')
    ordering = ('id',)

admin.site.register(Category, CategoryAdmin)

admin.site.register(AddVehicle, AddVehicleAdmin)
