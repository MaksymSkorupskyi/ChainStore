# Generated by Django 2.0.7 on 2018-07-06 11:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20180705_0953'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('males', django.db.models.manager.Manager()),
            ],
        ),
    ]
