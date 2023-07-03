from django.db import models
from accounts.models import CustomUser

class ContactUs(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='contact_us_entries'
    )
    name = models.CharField(max_length=100, verbose_name='Name')
    message = models.CharField(max_length=1000, verbose_name='Message')
    mobile = models.BigIntegerField(verbose_name='Mobile')
    
    def __str__(self):
        return f"ContactUs: {self.user.email} - {self.name}"

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us Entries'
