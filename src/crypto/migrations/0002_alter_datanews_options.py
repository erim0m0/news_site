# Generated by Django 4.0.6 on 2022-08-22 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datanews',
            options={'ordering': ('-id',), 'verbose_name': 'crypto', 'verbose_name_plural': 'crypto'},
        ),
    ]
