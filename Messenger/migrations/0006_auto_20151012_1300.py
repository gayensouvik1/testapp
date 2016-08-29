# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messenger', '0005_user_logged_in'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='receiver',
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(default=b'shivam', max_length=100),
        ),
    ]
