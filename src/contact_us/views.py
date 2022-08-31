# Create your views here.
from django.views.generic import TemplateView


class ContactUs(TemplateView):
    template_name = 'contact_us/contact_us.html'
