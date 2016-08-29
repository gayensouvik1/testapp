# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messenger', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_text',
            field=models.TextField(default=b'your message'),
        ),
    ]
