# Generated by Django 4.0.6 on 2022-08-27 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ('-id',), 'verbose_name': 'notification', 'verbose_name_plural': 'notifications'},
        ),
    ]
