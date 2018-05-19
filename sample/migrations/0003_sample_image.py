# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_auto_20180518_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='image',
            field=models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True),
        ),
    ]
