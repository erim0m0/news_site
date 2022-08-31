from django.urls import path
from forex import views

urlpatterns = [
    path('news/', views.ForexNews.as_view(), name='forex_news_page'),
    path('prices/', views.ForexPrices.as_view(), name='forex_prices_page'),
]
