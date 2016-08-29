# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messenger', '0003_message_message_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(max_length=100),
        ),
    ]
