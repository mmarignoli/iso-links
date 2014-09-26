# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_auto_20140926_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link_to',
            field=models.URLField(max_length=255),
        ),
    ]
