from django.db import models
from django.utils.translation import gettext_lazy as _


class ForexData(models.Model):
    price_name = models.CharField(
        max_length=10,
        verbose_name=_('price_name')
    )
    price = models.FloatField(
        verbose_name=_('price'),
        blank=True, null=True
    )

    def __str__(self):
        return self.price_name

    class Meta:
        verbose_name = _('Forex')
        verbose_name_plural = _('Forex')
