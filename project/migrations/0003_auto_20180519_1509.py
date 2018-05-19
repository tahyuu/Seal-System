# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20180519_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='doc_name',
            new_name='doc_number',
        ),
        migrations.AddField(
            model_name='document',
            name='doc_type',
            field=models.CharField(default=b'TI', max_length=20, choices=[(b'TI', 'TI'), (b'ME', 'ME'), (b'Source Code', 'Source Code')]),
        ),
    ]
