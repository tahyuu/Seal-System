# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0003_sample_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='image',
            field=models.ImageField(upload_to=b'photos/%Y/%m/%d'),
        ),
    ]
