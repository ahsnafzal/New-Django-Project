from django.db import models

# Create your models here.

class Voice(models.Model):
    name = models.CharField(max_length=100)
    voice_id = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=100, default=None)
    
    
class ProfanityWord(models.Model):
    word = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    