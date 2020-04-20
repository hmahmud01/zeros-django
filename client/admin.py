from django.contrib import admin

from client.models import Clients, FoodItems, Images
# Register your models here.
admin.site.register(Clients)
admin.site.register(FoodItems)
admin.site.register(Images)