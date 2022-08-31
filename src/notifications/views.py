from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from notifications.models import Notification


class NotificationView(ListView):
    model = Notification
    template_name = 'notifications/notifs.html'
    queryset = Notification.objects.filter(is_active=True)
    context_object_name = 'notifications'
