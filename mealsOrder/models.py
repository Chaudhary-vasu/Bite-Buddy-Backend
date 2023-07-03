import uuid
from django.db import models
from django.utils.safestring import mark_safe

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
    description = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="meals/", blank=True, null=True)
    price = models.FloatField()
    
    def meals_image(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height = "100"/>'.format(self.image.url))
        return None
    meals_image.short_description = "Meal Image"
    meals_image.allow_tags = True
    
    def __str__(self):
        return self.name

    
class Orders(models.Model):
    ordered_meals = models.ForeignKey(MealsItems,on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"Order by {self.user.user} - Meal: {self.ordered_meals.name}"
    

