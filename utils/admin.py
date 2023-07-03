from django.contrib import admin
from .models import ContactUs

# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['user','name','message','mobile']
admin.site.register(ContactUs,ContactUsAdmin)