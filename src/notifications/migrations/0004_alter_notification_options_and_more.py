# Generated by Django 4.0.6 on 2022-07-25 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0003_notification_create_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-id'], 'verbose_name': 'notification', 'verbose_name_plural': 'notifications'},
        ),
        migrations.AlterField(
            model_name='notification',
            name='create_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ایجادکننده'),
        ),
    ]
