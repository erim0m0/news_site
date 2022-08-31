import jdatetime
from django.dispatch import receiver
from users.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save


class Notification(models.Model):
    create_by = models.ForeignKey(
        User, blank=True,
        null=True, on_delete=models.CASCADE,
        editable=False, verbose_name='ایجادکننده'
    )
    title = models.CharField(
        max_length=70, verbose_name='تیتر اطلاعیه'
    )
    image = models.ImageField(
        upload_to='images/notifications', null=True,
        blank=True, verbose_name='عکس اطلاعیه'
    )
    text = RichTextField(
        verbose_name='متن اطلاعیه'
    )
    create_date = models.CharField(
        max_length=20, editable=False,
        verbose_name='تاریخ ایجاد شده'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='فعال / غیرفعال'
    )

    class Meta:
        ordering = ('-id',)
        indexes = [models.Index(fields=["title", "text", "image"])]
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Notification)
def save_create_by(sender, instance, **kwargs):
    if kwargs.get('signal'):
        instance.create_date = str(
            jdatetime.datetime.now().strftime('%H:%M _ %y/%m/%d')
        )[:19]
