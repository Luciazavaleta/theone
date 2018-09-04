# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='clasificacion',
            field=models.CharField(choices=[('A pagar', 'A pagar'), ('Pagos', 'Pagos')], max_length=20, default='A pagar'),
        ),
    ]
