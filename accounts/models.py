from django.db import models
from django.contrib.auth.models import User

#ORM은 단수형으로
class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)