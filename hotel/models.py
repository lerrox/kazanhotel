from django.db import models

# Create your models here.

class Hotel (models.Model):
    name = models.CharField(max_lenght=100)
    
    # ----------- address block
    city = models.CharField(max_lenght=50)
    street = models.CharField(max_length = 100)
    house = models.CharField(max_lenght = 20)
    geoDescription = models.TextField
      
    # ----------- contract block перенести в другой класс?
    #номер договора
    contractData = models.CharField(max_length = 500)
    contractDateFrom = models.DateField
    contractDateTo = models.DateField
    #условия договора - например условия предоставления скидки
    contractTerms = models.TextField
    discountMin = models.IntegerField
    discountMax = models.IntegerField
    discountValue = models.IntegerField
    contactManagerName = models.CharField
    contactManagerPhone = models.CharField
    contectManagerMail = models.EmailField
    

    
    