from django.shortcuts import render

from django.views.generic import FormView, RedirectView, TemplateView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import get_user_model

User = get_user_model()


from .forms import LoginForm

from core.applications.models import Applications


class Login(FormView):

	template_name = 'dashboard/login.html'

	form_class = LoginForm

	success_url = "/dashboard"


	def dispatch(self, request, *args, **kwargs):

		if request.user.is_authenticated():

			return HttpResponseRedirect(self.get_success_url())

		else:

			return super(Login, self).dispatch(request, *args, **kwargs)


	def form_valid(self, form):

		login(self.request, form.get_user())

		return super(Login, self).form_valid(form)



class Logout(RedirectView):

	pattern_name = 'Dashboard'

	def get(self, request, *args, **kwargs):

		logout(request)

		return super(Logout, self).get(self, *args, **kwargs)




class LoginRequiredMixin(object):

	def dispatch(self, request, *args, **kwargs):

		if not request.user.is_authenticated():

			return HttpResponseRedirect(reverse('Login'))

		else:

			return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)





class Dashboard(LoginRequiredMixin, TemplateView):

	template_name = 'dashboard/dashboard.html'


	def get_context_data(self, **kwargs):

		context = super(Dashboard, self).get_context_data(**kwargs)

		context['notifications_count'] = Applications.objects.filter(user=self.request.user).count()

		context['notifications'] = Applications.objects.filter(user=self.request.user)

		context['users'] = User.objects.all()

		return context
