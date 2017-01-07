from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models



class AccountManager(BaseUserManager):

	def create_user(self, email, password=None, **kwargs):

		if not email:

			raise ValueError('No es un email valido')

		if not kwargs.get('username'):

			raise ValueError('No existe el usuario')

		account = self.model(
			email = self.normalize_email(email), username=kwargs.get('username')
			)

		account.set_password(password)

		account.save()

		return account


	def create_superuser(self, email, password, **kwargs):

		account = self.create_user(email, password, **kwargs)

		account.is_admin = True

		account.is_staff = True

		account.save()

		return account



class Roles(models.Model):

	name = models.CharField(max_length=75)

	def __unicode__(self):

		return self.name


class Account(AbstractBaseUser):

	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)

	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)

	role = models.CharField(max_length=40, blank=True)

	is_admin = models.BooleanField(default=False)

	is_staff = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	objects = AccountManager()

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['username']

	def __unicode__(self):

		return self.email


	def get_full_name(self):

		return ' '.join([self.first_name, self.last_name])

	def get_short_name(self):

		return self.first_name


	