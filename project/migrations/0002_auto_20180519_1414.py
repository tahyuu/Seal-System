# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='address',
            new_name='doc_address',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='name',
            new_name='doc_name',
        ),
        migrations.RemoveField(
            model_name='document',
            name='image',
        ),
    ]
