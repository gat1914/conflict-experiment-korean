# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2021-03-26 17:18
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('control1', '0004_auto_20210326_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='send_answer',
            field=otree.db.models.StringField(choices=[['A', '나는 A를 선택합니다.'], ['B', '나는 B를 선택합니다.']], max_length=10000, null=True, verbose_name='What message do you want to send to First Person?'),
        ),
    ]
