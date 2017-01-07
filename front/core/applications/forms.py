from django import forms

from .models import *


class ApplicationsFormAdd(forms.Form):

	job_position = forms.CharField(
		required=True,
		max_length=75,
		label="",
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder': 'Cargo Solicitado'
			}))

	num_vacancies = forms.CharField(
		required=True,
		max_length=75,
		label="",
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Numero de Vacantes'
			}))

	type_position = forms.ModelChoiceField(
		queryset=JobType.objects.all(),
		label="Tipo de Posicion",
		required=True,
		widget=forms.Select(
			attrs={
			'class':'btn btn-success dropdown-toggle',
			}))


	workday = forms.ModelChoiceField(
		queryset=WorkDay.objects.all(),
		label="Jornada de Trabajo",
		required=True,
		widget=forms.Select(
			attrs={
			'class':'btn btn-success dropdown-toggle',
			}))

	salary = forms.CharField(
		required=True,
		max_length=75,
		label="",
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Salario'
			}))

	comments = forms.CharField(
		required=False,
		max_length=400,
		label="",
		widget=forms.Textarea(
			attrs={
			'cols': 80,
			'rows': 20}))


	def save(self):

		Profiles = Applications(
			job_position = self.cleaned_data['job_position'],
			num_vacancies = self.cleaned_data['num_vacancies'],
			type_position = self.cleaned_data['type_position'],
			workday = self.cleaned_data['workday'],
			salary = self.cleaned_data['salary'],
			comments = self.cleaned_data['comments'],
		)

		Profiles.user = self.user
		Profiles.save()




class JobFormAdd(forms.Form):

	name = forms.CharField(
		label="",
		required=True,
		max_length=75,
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Tipo de Cargo'
			}))


	def save(self):

		Type = JobType (
			name = self.cleaned_data['name']

		)

		Type.user = self.user
		Type.save()


class WorkFormAdd(forms.Form):

	name = forms.CharField(
		label="",
		required=True,
		max_length=75,
		widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Tipo de Jornada'
			}))


	def save(self):

		Type = WorkDay (
			name = self.cleaned_data['name']

		)

		Type.user = self.user
		Type.save()