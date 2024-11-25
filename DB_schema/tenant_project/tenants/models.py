from django.db import models

class Tenant(models.Model):
   name = models.CharField(max_length=100, unique=True)
   
   def __str__(self):
       return self.name

class Product(models.Model):
   tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
   name = models.CharField(max_length=200)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   
   def __str__(self):
        return f"{self.name} - ${self.price}"