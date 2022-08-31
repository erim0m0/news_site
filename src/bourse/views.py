from django.views.generic import TemplateView
from bourse.models import BrsDataNews


class BourseNews(TemplateView):
    template_name = 'bourse/bourse_news.html'

    def get_context_data(self, **kwargs):
        context = super(BourseNews, self).get_context_data(**kwargs)
        get_data = BrsDataNews.objects.all()
        context['slider_data'] = get_data.filter(place_news="carousel1")[:4]
        context['extra_slider_data'] = get_data.filter(place_news="box173")[:2]
        context['right_news_data'] = get_data.filter(place_news="box172")[1]
        context['left_news_data'] = get_data.filter(place_news="box172")[2:5]
        context['last_news_data1'] = get_data.filter(place_news="box157")[:5]
        context['last_news_data2'] = get_data.filter(place_news="box157")[5:10]
        return context


class BoursePrices(TemplateView):
    template_name = 'bourse/bourse_prices.html'
