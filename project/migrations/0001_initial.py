# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('address', models.CharField(unique=True, max_length=64)),
                ('city', models.CharField(max_length=32)),
                ('state_province', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('contact', models.CharField(max_length=32)),
                ('contact_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'images')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('project_state', models.CharField(default=b'quoting', max_length=20, choices=[(b'quoting', '\u62a5\u4ef7\u4e2d'), (b'onging', '\u5f00\u53d1\u4e2d'), (b'sustaining', '\u7ef4\u62a4\u4e2d'), (b'finished', '\u5df2\u5b8c\u6210')])),
                ('customer', models.ForeignKey(to='project.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='sample',
            field=models.ForeignKey(to='project.Project'),
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(to='project.Project'),
        ),
    ]
