from django.urls import path

from contact_us import views

urlpatterns = [
    path('', views.ContactUs.as_view(), name='contact_us_page')
]
