# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.
NAME_REGEX = re.compile(r'^[A-Za-z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
	def reg_validator(self,postData):
		errors = {}
		if 'first_name' not in postData or not NAME_REGEX.match(postData['first_name']):
			errors['first_name'] = "Please enter a valid first name"
		if 'last_name' not in postData or not NAME_REGEX.match(postData['last_name']):
			errors['last_name'] = "Please enter a valid last name"
		if 'email' not in postData or not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Please enter a valid email"
		if 'password' not in postData or len(postData['password']) < 8:
			errors['password'] = "Password must have at least 8 charactors"
		elif 'confirm' not in postData or postData['password']!=postData['confirm']:
			errors['password'] = "Please confirm your password"
		return errors

class User(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
	def __str__(self):
		return "<User object {} {} {}".format(self.first_name, self.last_name, self.email)