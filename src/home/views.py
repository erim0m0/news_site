from django.shortcuts import render
from django.views.generic import TemplateView
from notifications.models import Notification
from crypto.models import CrptDataNews
from bourse.models import BrsDataNews
from forex.models import ForexData


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def setup(self, request, *args, **kwargs):
        self.forex_prices = ForexData.objects.only('price')
        self.brs_news = BrsDataNews.objects.all()[:3]
        self.crypto_news = CrptDataNews.objects.all()[:3]
        return super(HomeView, self).setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['notifs'] = Notification.objects.only('title')[:5]
        context['last_brs_news'] = self.brs_news[0]
        context['last_crypto_news'] = self.crypto_news[0]
        context['new_crypto_news'] = self.crypto_news
        context['new_brs_news'] = self.brs_news
        context['forex_prices1'] = self.forex_prices[0]
        context['forex_prices2'] = self.forex_prices[1]
        return context


def site_header_component(request):
    return render(request, 'shared/site_header_components.html')


def site_footer_component(request):
    return render(request, 'shared/site_footer_components.html')
