import uuid
from django.db import models

# Create your models here.
class Customer(models.Model):
    user = models.CharField(max_length=20,default="")
    street = models.CharField(max_length=100,default="")
    postalCode = models.IntegerField()
    city = models.CharField(max_length=100,default="")
    
    def __str__(self):
        return self.user
    
class MealsItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500,default="")
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    
class Orders(models.Model):
    ordered_meals = models.ForeignKey(MealsItems,on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"Order by {self.user.user} - Meal: {self.ordered_meals.name}"
    

