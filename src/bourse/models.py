from django.db import models


class BrsDataNews(models.Model):
    PLACE_NEWS_TYPE = (
        ("carousel1", "اسلایدر"),
        ("box173", "خبر کنار اسلایدر"),
        ("box172", "خبر فرابورس"),
        ("box157", "آخرین خبر")
    )

    place_news = models.CharField(
        max_length=30, choices=PLACE_NEWS_TYPE,
        verbose_name='مکان بارگزاری خبر'
    )
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

    def __str__(self):
        return self.place_news

    class Meta:
        ordering = ('id',)
        indexes = [models.Index(fields=[
            "place_news", "title_news", "img_news"
        ])]
        verbose_name = 'bourse'
        verbose_name_plural = 'bourse'
