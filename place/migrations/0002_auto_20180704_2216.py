# Generated by Django 2.0.7 on 2018-07-04 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('name',), 'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('name',), 'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='country',
            new_name='name',
        ),
    ]
