# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_auto_20160115_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='nome',
        ),
    ]
