# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portofolionew', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portofolio',
            old_name='sinopsis',
            new_name='desc',
        ),
    ]
