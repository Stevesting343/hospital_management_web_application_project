from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    type_user = models.CharField(max_length=20)
    speciality = models.CharField(max_length=20)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=250)
    email = models.CharField(max_length=150)
    gender = models.CharField(max_length=200)
    # age = models.IntegerField()


class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)


class Appointment(models.Model):
    enter_full_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    d_id = models.IntegerField()
    p_id = models.IntegerField()


class Accepted_Data(models.Model):
    enter_full_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    d_id = models.IntegerField()
    p_id = models.IntegerField()
    date = models.CharField(max_length=50)
