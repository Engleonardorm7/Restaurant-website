from django.db import models


# Create your models here.

class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image=models.ImageField( upload_to='media/')

    def __str__(self):
        return self.name

class Booking(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    guest_number=models.IntegerField()
    comment=models.TextField(max_length=500)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'