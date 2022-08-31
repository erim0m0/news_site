from django.db import models


class CrptDataNews(models.Model):
    title_news = models.CharField(
        max_length=100, verbose_name='تیتر خبر'
    )
    img_news = models.CharField(
        max_length=300, blank=True, null=True,
        verbose_name='آدرس عکس خبر'
    )
    url_news = models.CharField(
        max_length=500, verbose_name='آدرس خبر'
    )
    datetime = models.CharField(
        max_length=50, verbose_name='ساعت انتشار'
    )
    text = models.CharField(
        max_length=500, verbose_name='متن کوتاه خبر'
    )

    def __str__(self):
        return self.title_news

    class Meta:
        ordering = ('-id',)
        indexes = [models.Index(fields=[
            "title_news", "img_news", "text"
        ])]
        verbose_name = 'crypto'
        verbose_name_plural = 'crypto'
