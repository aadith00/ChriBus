from django.db import models

# Create your models here.

class rent(models.Model):
    name : models.CharField(max_length=100)
    price : models.IntegerField()


class VehicleRental(models.Model):
    ownerName = models.CharField(max_length=255)
    vehicleType = models.CharField(max_length=50)
    vehicleModel = models.CharField(max_length=255)
    rentalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    imageUpload = models.ImageField(upload_to='upload')
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject
