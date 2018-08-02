# Generated by Django 2.1 on 2018-08-02 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_auto_20180802_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='version',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='version'),
        ),
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
