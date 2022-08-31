from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ForexNews(TemplateView):
    template_name = 'forex/forex_news.html'


class ForexPrices(TemplateView):
    template_name = 'forex/forex_price.html'
