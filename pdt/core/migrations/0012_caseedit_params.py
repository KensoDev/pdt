# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150527_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseedit',
            name='params',
            field=jsonfield.fields.JSONField(default=None),
        ),
    ]
