from django.contrib import admin
from michelinyelp.restaurant.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating']
