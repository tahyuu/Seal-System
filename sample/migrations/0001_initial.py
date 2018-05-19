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
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('input_date', models.DateField(auto_now_add=True)),
                ('product_state', models.CharField(default=b'wait_sealing', max_length=20, choices=[(b'sealed', '\u5df2\u9500\u6bc1'), (b'wait_sealing', '\u5f85\u9500\u6bc1'), (b'checkout', '\u88ab\u501f\u51fa')])),
                ('customer', models.ForeignKey(to='sample.Customer')),
                ('department', models.ManyToManyField(to='sample.Department')),
            ],
        ),
    ]
