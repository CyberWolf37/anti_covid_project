from django.db import models
from datetime import datetime
from .forms import FightForm

# Create your models here.
class information(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

class article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField()

class userFighting(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    socialSecurity = models.BigIntegerField()
    created_at = models.DateTimeField()

    @classmethod
    def create(cls, form:FightForm ):
        name = form.cleaned_data['name']
        lastname = form.cleaned_data['lastname']
        email = form.cleaned_data['email']
        socialSecurity = form.cleaned_data['social_security_usr']
        created_at = datetime.now()

        profil = cls(name=name, lastname=lastname, email=email, socialSecurity=socialSecurity ,created_at=created_at)
        return profil