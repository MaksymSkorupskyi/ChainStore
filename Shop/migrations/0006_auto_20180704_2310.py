# Generated by Django 2.0.7 on 2018-07-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20180704_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(max_length=250),
        ),
    ]
