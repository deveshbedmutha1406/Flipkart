from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255, null=False)
    body  = models.CharField(max_length=255, null=False)
    tag = models.CharField(max_length=255, null=False)




