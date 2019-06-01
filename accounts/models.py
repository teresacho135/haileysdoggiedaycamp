from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model) :
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  profile_picture = models.CharField(max_length=100, null=True, blank=True)
  vet_info = models.TextField()
  contact_info= models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return self.user.email
