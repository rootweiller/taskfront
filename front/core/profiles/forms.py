# -*- coding: utf-8 -*-

from django import forms

from .models import Roles, Account
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterUserForm(forms.Form):

	first_name = forms.CharField(label="", required=True, max_length=75,
		widget=forms.TextInput(attrs={'class': 'form-control',
			'placeholder': 'Nombres'}))

	last_name = forms.CharField(label="", required=True, max_length=75,
		widget=forms.TextInput(attrs={'class': 'form-control',
			'placeholder': 'Apellidos'}))

	email = forms.CharField(label="", required=True, max_length=75,
		widget=forms.TextInput(attrs={'class': 'form-control',
			'placeholder': 'Email'}))

	username = forms.CharField(label="", required=True, max_length=75,
		widget=forms.TextInput(attrs={'class': 'form-control',
			'placeholder': 'Nickname'}))

	role = forms.ModelChoiceField(
		queryset=Roles.objects.all(),
		label="Rol",
		widget=forms.Select(
			attrs={
			'class': 'btn btn-success dropdown-toggle'
			}))

	passwordnew	= forms.CharField(label="",required=True,
		widget=forms.PasswordInput(render_value=True, 
			attrs={'class': 'form-control', 'name': 'passwordnew',
	 		'placeholder': 'Contraseña'}))

	passwordverify = forms.CharField(label="",required=True,
		widget=forms.PasswordInput(render_value=True,
			attrs={'class': 'form-control', 'name': 'passwordverify',
			'placeholder': 'Nuevamente la contraseña'}))


	class Meta:

		model = Account




	def clean_passwordverify(self):

		cleaned_data = self.cleaned_data

		password = cleaned_data.get('passwordnew')
		passwordveri = cleaned_data.get('passwordverify')

		if len(password) < 4:
			raise forms.ValidationError('La contraseña debe ser mayor'
				'de 4 caracteres')

		if password != passwordveri:
			raise forms.ValidationError('Las contraseñas no coinciden')

	def clean_username(self):
		username = self.cleaned_data.get('username')

		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Usuario ya Registrado')

	def clean_email(self):
		email = self.cleaned_data.get('email')

		try:
			User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Correo Electrónico ya registrado')

	def save(self):
		user = User.objects.create_user(
			username=self.cleaned_data['username'],
			email=self.cleaned_data['email'], 
			password=self.cleaned_data['passwordnew']
		)

		Profile = User (
			role = self.cleaned_data['role'],
		)

		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.is_active = True	
		user.is_staff = False
		user.is_admin = False
		Profile.save()
		user.save()





class RolFormAdd(forms.Form):

	name = forms.CharField(
		label="",
		required=True,
		max_length=75,
		widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'Rol'
			}))


	def save(self):

		Profile = Roles (
			name = self.cleaned_data['name']
		)

		Profile.save()