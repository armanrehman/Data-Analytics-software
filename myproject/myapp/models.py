from django.db import models

# Create your models here.
#inherits from django models for creating model 
class Data(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    rent = models.IntegerField()
    emi = models.IntegerField()
    tax = models.IntegerField()
    exp = models.IntegerField()
    expenses_monthly = models.IntegerField(default=0)
    income_monthly = models.IntegerField(default=0)
