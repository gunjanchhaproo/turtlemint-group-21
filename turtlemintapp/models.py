from django.db import models

class Motor(models.Model):
    carName=models.CharField(max_length=100)
    carNumber=models.CharField(max_length=200)
    registrationYear=models.CharField(max_length=10)
    variantOfCar=models.CharField(max_length=200)

class MotorInsurance(models.Model):
    carId=models.ForeignKey(Motor,on_delete=models.CASCADE,default=1)
    bankName=models.CharField(max_length=100)
    insuranceType=models.CharField(max_length=200)
    premium=models.BigIntegerField(default=0)
    yearly=models.BigIntegerField(default=1)
    benefits1=models.SmallIntegerField(default=0)
    benefits2=models.SmallIntegerField(default=0)
    benefits3=models.SmallIntegerField(default=0)
    benefits4=models.SmallIntegerField(default=0)
    depriciationValue=models.BigIntegerField(null='True')
    


# Create your models here.
