from django.urls import path

from notifications import views

urlpatterns = [
    path('', views.NotificationView.as_view(), name='notifs_page')
]
