# Generated by Django 4.0.6 on 2022-08-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0003_alter_forexdata_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forexdata',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='price'),
        ),
    ]
