# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portofolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('sinopsis', models.TextField(null=True, blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
