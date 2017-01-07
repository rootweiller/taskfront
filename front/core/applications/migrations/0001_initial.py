# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 18:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_position', models.CharField(max_length=75)),
                ('num_vacancies', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('comments', models.CharField(max_length=400)),
                ('datecreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationsMV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('comments', models.CharField(blank=True, max_length=400, null=True)),
                ('datecreated', models.DateTimeField(auto_now_add=True)),
                ('applications', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.Applications')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='applications',
            name='type_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.JobType'),
        ),
        migrations.AddField(
            model_name='applications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applications',
            name='workday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.WorkDay'),
        ),
    ]