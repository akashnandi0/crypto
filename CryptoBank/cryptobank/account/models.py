from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class CreateAccount(models.Model):
    personname=models.CharField(max_length=120)
    accno=models.CharField(max_length=15,unique=True)
    # acctype=models.CharField(max_length=120)
    balance=models.IntegerField(default=300)
    phonenumber=models.CharField(max_length=12,unique=True)
    mpin=models.CharField(max_length=6,unique=True)

    def __str__(self):
        return self.personname

# class CreateAccount(models.Model):
#     personname=models.CharField(max_length=120)
#     accno=models.CharField(max_length=15)
#     balance=models.IntegerField(default=300)
#     phonenumber=models.CharField(max_length=12)
#     mpin=models.CharField(max_length=6,unique=True)
#
#     def __str__(self):
#         return self.personname


class Transferdetails(models.Model):
    mpin=models.CharField(max_length=6)
    accno=models.CharField(max_length=15)
    amount=models.IntegerField()

    def __str__(self):
        return self.mpin+ self.accno