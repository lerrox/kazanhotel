#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User


# инфа о договоре с отелем и условиях сотрудничества
class ContractWithHotel(models.Model):
    # номер договора
    contractData = models.CharField(max_length = 500)
    contractDateFrom = models.DateField
    contractDateTo = models.DateField
    # условия договора - например условия предоставления скидки
    contractTerms = models.TextField
    discountMin = models.IntegerField
    discountMax = models.IntegerField
    discountValue = models.IntegerField
    
    def __unicode__(self):
        return "контакт №{0}".format(self.contractData)

# описываем отель
class Hotel (models.Model):
    # описание отеля
    name = models.CharField(max_lenght=100)
    descriptions = models.TextField
    stars = models.IntegerField
    contract = models.ForeignKey(ContractWithHotel)
    
    # адрес отеля
    city = models.CharField(max_lenght=50)
    street = models.CharField(max_length = 100)
    house = models.CharField(max_lenght = 20)
    geoDescription = models.TextField(blank = True, null = True)
    
    # как связаться с отелем
    phone = models.CharField(blank = True, null = True)
    email = models.EmailField(blank = True, null = True)
    web = models.URLField(blank = True, null = True)
      
    # контактное лицо
    contactManagerName = models.CharField(blank = True, null = True)
    contactManagerPhone = models.CharField(blank = True, null = True)
    contectManagerMail = models.EmailField(blank = True, null = True)
    
    def __unicode__(self):
        return "отель {0}".format(self.name)
  
# Тип номера  
class RoomType(models.Model):
    name = models.CharField
    description = models.TextField(null = True, blank = True)
    icon = models.ImageField(blank = True, null = True)
    
    def __unicode__(self):
        return "тип комнаты {0}".format(self.name)
    
# Номер отеля
class Room(models.Model):
    description = models.TextField
    type = models.ForeignKey(RoomType)
    hotel  = models.ForeignKey(Hotel)
    
    def __unicode__(self):
        return "комната в {0}: {1}".format(self.hotel.name, self.type.name)
    
# Картинка для отеля или комнаты в отеле
class Image(models.Model):   
    url = models.URLField
    thumbUrl = models.URLField
    hotel = models.ForeignKey(Hotel, null = True)
    room = models.ForeignKey(Room, null = True)
    
    def __unicode__(self):
        name = ''
        if self.hotel != None: 
            name = self.hotel.name
        if self.room: 
            name = self.room.type.name
        return "картинка {0} для {1}".format(name)
    
# Описание дополнительной услуги отеля 
class HotelService(models.Model):
    title = models.CharField
    description = models.TextField
    icon = models.ImageField
    hotel = models.ForeignKey(Hotel)
    
    def __unicode__(self):
        return "услуга в отеле '{0}'".format(self.title)
 
# бстрактный заказ чего нить   
class Order(models.Model):
    created = models.DateTimeField
    orderFrom = models.DateTimeField
    orderTo = models.DateTimeField
    client = models.ForeignKey(User)
    room = models.ForeignKey(Room, blank = True, null = True)
    comments = models.TextField
    
    def __unicode__(self):
        return "заказ от {0}".format(self.client.name)
    
# контактные и другие данные для юзера
class Profile(models.Model):
    user = models.ForeignKey(User)
    firstName = models.CharField
    lastName = models.CharField
    email = models.EmailField
    phone = models.CharField
    
    def __unicode__(self):
        return "{0} {1} profile".format(self.firstName, self.lastName)
    
    

    