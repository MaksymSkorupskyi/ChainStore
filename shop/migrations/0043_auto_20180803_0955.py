# Generated by Django 2.1 on 2018-08-03 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_auto_20180803_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shop_owner', to='person.Person', verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='sellers',
            field=models.ManyToManyField(related_name='sellers', to='person.Person', verbose_name='sellers'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='warehouses',
            field=models.ManyToManyField(to='warehouse.Warehouse', verbose_name='warehouses'),
        ),
    ]
