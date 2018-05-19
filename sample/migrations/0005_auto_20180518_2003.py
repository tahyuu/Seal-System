# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0004_auto_20180518_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='image',
            new_name='image_data',
        ),
    ]
