# -*- coding: utf-8 -*-
from django.contrib import admin
from hotel.models import *

class HotelServInline(admin.StackedInline):
    model = HotelService
    extra = 1
    can_delete = True
    
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    can_delete = True
    
class RoomInline(admin.TabularInline):
    model = Room
    extra = 1
    can_delete = True

class HotelAdmin(admin.ModelAdmin):
    list_display = [ 'name',  'stars', 'street', 'house']
    ordering = ['stars']
    fieldsets = (
                 (None,{'fields':['name', 'descriptions', 'stars', 'contract']}),
                 ('Расположение',{'fields':['city', 'street', 'house', 'geoDescription']}),
                 ('Контакты',{'fields':['phone', 'email', 'web', 
                                            'contactManagerName', 
                                            'contactManagerPhone', 
                                            'contectManagerMail']})
                 )
    inlines = [
        HotelServInline,
        ImageInline,
        RoomInline,
    ]


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelService)
admin.site.register(Image)
admin.site.register(Room)
admin.site.register(ContractWithHotel)
admin.site.register(RoomType)