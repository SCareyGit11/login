from __future__ import unicode_literals
from django.core.validators import EmailValidator
from django.db import models

# Create your models here.



class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.EmailField(max_length=255, validators=[EmailValidator])
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)