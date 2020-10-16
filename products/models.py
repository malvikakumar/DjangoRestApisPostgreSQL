from django.db import models

# Create your models here.


class Product(models.Model):
    class ProductType(models.TextChoices):
        Mobile = 'M'
        Laptop = 'L'

    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    # image = models.ImageField(upload_to="Blob", blank=True, null=True)
    type = models.CharField(
        max_length=1,
        choices=ProductType.choices,
        default=ProductType.Mobile,
    )
    ram = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    processor = models.CharField(max_length=50, blank=True, null=True)
    hdCapacity = models.CharField(max_length=50, blank=True, null=True)
    screenSize = models.CharField(max_length=50, blank=True, null=True)
