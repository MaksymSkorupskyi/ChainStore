# Generated by Django 2.0.7 on 2018-07-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_auto_20180704_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
