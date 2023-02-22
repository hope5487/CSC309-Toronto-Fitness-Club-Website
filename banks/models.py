from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL


# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=200)
    swift_code = models.CharField(max_length=200)
    inst_num = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    bank = models.ForeignKey(to=Bank, on_delete=SET_NULL, null=True)
    name = models.CharField(max_length=200)
    transit_num = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(default="admin@utoronto.ca")
    capacity = models.PositiveIntegerField(null=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
