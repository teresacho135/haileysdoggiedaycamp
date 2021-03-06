from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User
# Create your models here.

class Camper(models.Model):
  pet_name = models.CharField(max_length=100)
  age = models.IntegerField()
  isActive = models.BooleanField(default = False)
  food_amount = models.CharField(max_length=100)
  medicine = models.TextField()
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='camper')

  def __str__(self):
    return self.pet_name


class Schedule(models.Model):
  start_time = models.TimeField(default='20:00')
  end_time = models.TimeField(default='20.00')
  camper = models.ForeignKey(Camper, on_delete=models.CASCADE, related_name='camper')

  def __str__(self):
    return self.days

class Payment(models.Model):
  schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='schedule')
  paid = models.BooleanField(default = False)

  def __str__(self):
    return self.paid
