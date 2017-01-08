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



class ApplyApproveForm(forms.Form):


	BOOL_CHOICES = (
		(True, 'Approve'),
		(False, 'Rejected')
	)

	applications = forms.ModelChoiceField(
		queryset = Applications.objects.all(),
		label = "Aplicaciones por Aprobar",
		widget = forms.Select(
			attrs = {
			'class': 'btn btn-success dropdown-toogle'
			}))
	
	status = forms.BooleanField(
		label="Aprobar o Rechazar",
		widget=forms.CheckboxInput())
	
	comments = forms.CharField(
		max_length=400,
		label="",
		widget=forms.Textarea(
			attrs={
			'cols': 80,
			'rows': 20}))


	def clean(self):

		if self.cleaned_data.get('status', False):

			self.fields['comments'].required=True,
			self.fields['applications'].required=True,

			self._clean_fields()

		return self.cleaned_data



	def save(self):

		Profile = ApplicationsMV (
			applications = self.cleaned_data['applications'],
			status = self.cleaned_data['status'],
			comments = self.cleaned_data['comments'],
		)

		Profile.user = self.user
		Profile.save()