# Generated by Django 2.0.7 on 2018-07-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20180704_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('first_name', 'last_name'), 'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True, verbose_name='e-mail'),
        ),
    ]
