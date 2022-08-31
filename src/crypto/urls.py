from django.urls import path

from crypto import views

urlpatterns = [
    path('prices/', views.CryptoPrices.as_view(), name='crypto_prices_page'),
    path('news/', views.CryptoNews.as_view(), name='crypto_news_page'),
]
