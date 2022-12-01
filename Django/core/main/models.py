from django.db import models

# Create your models here.
class Contacts(models.Model):
    phone = models.CharField("Phone number: ", max_length=15)
    e_mail = models.CharField("E-Mail", max_length=30)

    def __str__(self) -> str:
        return 'Contacts'

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
