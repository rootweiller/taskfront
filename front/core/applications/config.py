from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import FormView

from .forms import JobFormAdd, WorkFormAdd


class JobtypeAdd(FormView):

	template_name = 'core/applications/jobtypeadd.html'

	form_class = JobFormAdd

	success_url = '/dashboard'


	def post(self, request, *args, **kwargs):

		form_class = self.get_form_class()

		form = self.get_form(form_class)

		if form.is_valid():


			return self.form_valid(form, **kwargs)

		else:

			return self.form_invalid(form, **kwargs)


	def form_invalid(self, form, **kwargs):

		context = self.get_context_data(form=form)

		return self.render_to_response(context)


	def form_valid(self, form, **kwargs):

		context = self.get_context_data(**kwargs)

		context['form'] = form

		form.user = self.request.user
		form.save()

		return HttpResponseRedirect(self.get_success_url())



class WorkdayAdd(FormView):

	template_name = 'core/applications/workday.html'

	form_class = WorkFormAdd

	success_url = '/dashboard'

	def post(self, request, *args, **kwargs):

		form_class = self.get_form_class()

		form = self.get_form(form_class)

		if form.is_valid():


			return self.form_valid(form, **kwargs)

		else:

			return self.form_invalid(form, **kwargs)


	def form_invalid(self, form, **kwargs):

		context = self.get_context_data(form=form)

		return self.render_to_response(context)


	def form_valid(self, form, **kwargs):

		context = self.get_context_data(**kwargs)

		context['form'] = form

		form.user = self.request.user
		form.save()

		return HttpResponseRedirect(self.get_success_url())