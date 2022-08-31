from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.

class User(AbstractUser):
    otp_code = models.PositiveIntegerField(
        blank=True, null=True,
        verbose_name='کد یکبار مصرف'
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(
        verbose_name=_('ip_address')
    )

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name = _('IP Address')
        verbose_name_plural = _('IP Addresses')


