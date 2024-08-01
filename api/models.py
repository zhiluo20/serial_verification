from django.db import models

# Create your models here.

class SerialNumber(models.Model):
    serial = models.CharField(max_length=100, unique=True)
    expiry_date = models.DateField()

    def __str__(self):
        return self.serial