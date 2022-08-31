from django.views.generic import TemplateView
from crypto.models import CrptDataNews


class CryptoPrices(TemplateView):
    template_name = 'crypto/crypto_prices.html'


class CryptoNews(TemplateView):
    template_name = 'crypto/crypto_news.html'

    def get_context_data(self, **kwargs):
        context = super(CryptoNews, self).get_context_data(**kwargs)
        context['crypto_news'] = CrptDataNews.objects.all()[:4]
        return context
