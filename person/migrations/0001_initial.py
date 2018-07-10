# Generated by Django 2.0.7 on 2018-07-04 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('birthdate', models.DateField(default=datetime.datetime.now)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
    ]