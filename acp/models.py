from django.db import models

# Create your models here.
class information(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=5000)

class article(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=5000)
    created_at = models.DateTimeField()

class userFighting(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    socialSecurity = models.BigIntegerField()
    created_at = models.DateTimeField()