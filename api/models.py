from django.db import models
from django.contrib.auth.models import User


class Taxi(models.Model):
    plate = models.CharField(max_length=100)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    coordX = models.DecimalField(max_digits=6, decimal_places=2)
    coordY = models.DecimalField(max_digits=6, decimal_places=2)


class TaxiRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        DECLINED = 'DECLINED', 'Declined'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=10, decimal_places=4)
    requestTime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status.choices,
                              default=Status.PENDING, max_length=100)
