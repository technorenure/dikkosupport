from django.db import models
from django.contrib.auth.models import User


class LocalGovt(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class RegType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class GroupType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.FileField(upload_to='gallery')


class Registeration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)
    home_address = models.CharField(max_length=200)
    ward = models.CharField(max_length=200)
    local_gov = models.ForeignKey(LocalGovt, on_delete=models.CASCADE)
    reg_type = models.ForeignKey(RegType, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name