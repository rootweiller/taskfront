from __future__ import unicode_literals

from django.db import models
from core.profiles.models import Account


class JobType(models.Model):

	user = models.ForeignKey(Account)
	name = models.CharField(max_length=75)


	def __unicode__(self):

		return self.name


class WorkDay(models.Model):

	user = models.ForeignKey(Account)
	name = models.CharField(max_length=75)

	def __unicode__(self):

		return self.name


class Applications(models.Model):

	user = models.ForeignKey(Account)
	job_position = models.CharField(max_length=75)
	num_vacancies = models.IntegerField()
	type_position = models.ForeignKey(JobType)
	workday = models.ForeignKey(WorkDay)
	salary = models.IntegerField()
	comments = models.CharField(max_length=400)
	datecreated = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):

		return self.job_position


BOOL_CHOICES = (
	(True, 'Approve'),
	(False, 'Rejected'))


class ApplicationsMV(models.Model):

	user = models.ForeignKey(Account)
	applications = models.ForeignKey(Applications)
	status = models.BooleanField(default=False)
	comments = models.CharField(max_length=400, blank=True, null=True)
	datecreated = models.DateTimeField(auto_now_add=True)



	def __unicode__(self):

		return self.status

