from django.db import models

# Create your models here.
# class Patient(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=20)


class Doctor(models.Model):
    #using = 'RegisterUsersdb'
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20) 



