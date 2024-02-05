from django.db import models
import string
import random

def generateRandomCode():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase),k=length)
        if Room.objects.filtter(code=code).count() == 0:
            break
# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=8, unique=True)
    guestCanPlay = models.BooleanField(null=False, default=False)
    createdAt = models.DateTimeField(auto_now_add=True)