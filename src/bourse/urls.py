from django.urls import path

from bourse import views

urlpatterns = [
    path('news/', views.BourseNews.as_view(), name='bourse_news_page'),
    path('prices/', views.BoursePrices.as_view(), name='bourse_prices_page'),
]
