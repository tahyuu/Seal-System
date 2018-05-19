# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('serialnumber', models.CharField(unique=True, max_length=64)),
                ('input_date', models.DateField(auto_now_add=True)),
                ('product_state', models.CharField(default=b'wait_sealing', max_length=20, choices=[(b'sealed', '\u5df2\u9500\u6bc1'), (b'wait_sealing', '\u5f85\u9500\u6bc1'), (b'checkout', '\u88ab\u501f\u51fa')])),
                ('customer', models.ForeignKey(to='sample.Customer')),
                ('department', models.ManyToManyField(to='sample.Department')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='department',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
