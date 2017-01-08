from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import FormView, DetailView, ListView


from .forms import ApplicationsFormAdd, ApplyApproveForm

from .models import Applications, ApplicationsMV

class ApplicationsAdd(FormView):

	template_name = 'core/applications/add.html'

	form_class = ApplicationsFormAdd

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




class ApplicationsDetail(DetailView):

	template_name = 'core/applications/listdetail.html'

	model = Applications

	context_object_name = 'applydetails'

	def get_context_data(self, **kwargs):

		context = super(ApplicationsDetail, self).get_context_data(**kwargs)

		context['applyall'] = self.model.objects.filter(user=self.request.user)

		return context



class ApplicationsAll(ListView):

	template_name = 'core/applications/listall.html'

	model = Applications

	context_object_name = 'listall'

	def get_context_data(self, **kwargs):

		context = super(ApplicationsAll, self).get_context_data(**kwargs)

		context['applyall'] = self.model.objects.filter(user=self.request.user)

		return context



class ApplicationsApprove(FormView):

	template_name = 'core/applications/approve.html'

	form_class = ApplyApproveForm

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



class ApplyApproveList(ListView):

	template_name = 'core/applications/approvelist.html'

	model = ApplicationsMV


	def get_context_data(self, **kwargs):

		context = super(ApplyApproveList, self).get_context_data(**kwargs)

		context['listall'] = ApplicationsMV.objects.all()

		return context