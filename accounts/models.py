from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
ROLE_CHOICES = (
    ('Admin','Admin'),
    ('Customer','Customer'),
)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(choices = ROLE_CHOICES,max_length=100,default='Customer', verbose_name=('Role (Admin/Customer)'))
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()
    
    def __str__(self):
        return str(self.email)