from django.db import models

# Create your models here.
class Emails(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    message =models.CharField(max_length=25000)

    def __str__ (self):
        return self.Emails
