#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User

    
def make_upload_path(instance, filename):
    """Generates upload path for FileField"""
    return u"media/img/%s" % ( filename)
    


# инфа о договоре с отелем и условиях сотрудничества
class ContractWithHotel(models.Model):
    contractData = models.CharField(max_length = 500)
    contractDateFrom = models.DateField()
    contractDateTo = models.DateField()
    # условия договора - например условия предоставления скидки
    contractTerms = models.TextField()
    discountMin = models.IntegerField()
    discountMax = models.IntegerField()
    discountValue = models.IntegerField()
    
    def __unicode__(self):
        return "contract {0}".format(self.contractData)

# описываем отель
class Hotel (models.Model):
    # описание отеля
    name = models.CharField(max_length=100, verbose_name = 'название')
    descriptions = models.TextField(verbose_name = 'описание')
    stars = models.IntegerField(verbose_name = 'звезд')
    contract = models.ForeignKey(ContractWithHotel, verbose_name = 'договор')
    
    # адрес отеля
    city = models.CharField(max_length=50, verbose_name = 'город')
    street = models.CharField(max_length = 100, verbose_name = 'улица')
    house = models.CharField(max_length=50, verbose_name = 'дом')
    geoDescription = models.TextField(blank = True, null = True, 
                                      verbose_name = 'описание расположения')
    
    # как связаться с отелем
    phone = models.CharField(blank = True, 
                             null = True, 
                             max_length=50,
                             verbose_name = 'телефон')
    email = models.EmailField(blank = True, 
                              null = True)
    web = models.URLField(blank = True, 
                          null = True,
                          verbose_name = 'дрес сайта')
      
    # контактное лицо
    contactManagerName = models.CharField(blank = True, 
                                          null = True, 
                                          max_length=50,
                                          verbose_name = 'ФИО менеджера ')
    contactManagerPhone = models.CharField(blank = True, 
                                           null = True, 
                                           max_length=50,
                                           verbose_name = 'телефон менеджера')
    contectManagerMail = models.EmailField(blank = True, 
                                           null = True, 
                                           max_length=70,
                                           verbose_name = 'email менеджера')
    
    def __unicode__(self):
        return "hotel {0}".format(self.name)
  
# Тип номера  
class RoomType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null = True, blank = True)
    icon = models.ImageField(blank = True, null = True, upload_to = "/img")
    
    def __unicode__(self):
        return "room type {0}".format(self.name)
    
# Номер отеля
class Room(models.Model):
    description = models.TextField()
    type = models.ForeignKey(RoomType)
    hotel  = models.ForeignKey(Hotel)
    
    def __unicode__(self):
        return "room {0}: {1}".format(self.hotel.name, self.type.name)
    
# Картинка для отеля или комнаты в отеле
class Image(models.Model):   
    url = models.ImageField(upload_to = make_upload_path)
    thumbUrl = models.ImageField(upload_to = make_upload_path)
    hotel = models.ForeignKey(Hotel, null = True)
    room = models.ForeignKey(Room, null = True)
    
    def __unicode__(self):
        name = ''
        if self.hotel != None: 
            name = self.hotel.name
        if self.room: 
            name = self.room.type.name
        return "pict {0} : {1}".format(name)
    
# Описание дополнительной услуги отеля 
class HotelService(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(upload_to = make_upload_path)
    hotel = models.ForeignKey(Hotel)
    
    def __unicode__(self):
        return "service '{0}'".format(self.title)
 
# бстрактный заказ чего нить   
class Order(models.Model):
    created = models.DateTimeField()
    orderFrom = models.DateTimeField()
    orderTo = models.DateTimeField()
    client = models.ForeignKey(User)
    room = models.ForeignKey(Room, blank = True, null = True)
    comments = models.TextField()
    
    def __unicode__(self):
        return "client {0}".format(self.client.name)
    
# контактные и другие данные для юзера
class Profile(models.Model):
    user = models.ForeignKey(User)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    
    def __unicode__(self):
        return "{0} {1} profile".format(self.firstName, self.lastName)
    
# моделька для статьи 
class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    keywords = models.TextField()
    menuname = models.CharField(max_length=50)
    published = models.BooleanField()
    
    def __unicode__(self):
        return "article {0}".format(self.title)
    
class Menu(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return "menu {0}".format(self.name)

    

    