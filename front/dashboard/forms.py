from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
	username = forms.CharField(required=True, max_length=75,
		label="",widget=forms.TextInput(
			attrs={'class' : 'form-control', 'placeholder': 'Usuario'}))
	password = forms.CharField(required=True, max_length=75,
		label="",widget= forms.PasswordInput(
			attrs={'class' : 'form-control', 'placeholder': 'Password'}))
