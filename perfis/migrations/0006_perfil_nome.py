# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_remove_perfil_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='nome',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
