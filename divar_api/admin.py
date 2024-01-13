from django.contrib import admin
from .models import House, HouseSpecifications, Seller
# Register your models here.


class HouseAdminPanel (admin.ModelAdmin):
    list_display = ['title', 'seller', 'total_price', 'city']
    list_filter = ['city', 'seller']
    search_fields = ['title']


class HouseSpecificationsAdminPanel (admin.ModelAdmin):
    list_display = ['name']


admin.site.register(House, HouseAdminPanel)
admin.site.register(HouseSpecifications, HouseSpecificationsAdminPanel)
admin.site.register(Seller)

