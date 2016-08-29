# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messenger', '0004_auto_20151010_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logged_in',
            field=models.BooleanField(default=False),
        ),
    ]
