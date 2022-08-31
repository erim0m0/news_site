# Generated by Django 4.0.6 on 2022-07-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bourse', '0002_alter_datanews_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datanews',
            name='img_news',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='آدرس عکس خبر'),
        ),
        migrations.AlterField(
            model_name='datanews',
            name='place_news',
            field=models.CharField(choices=[('carousel1', 'اسلایدر'), ('box173', 'خبر کنار اسلایدر'), ('box172', 'خبر فرابورس'), ('box157', 'آخرین خبر')], max_length=30, verbose_name='مکان بارگزاری خبر'),
        ),
    ]
