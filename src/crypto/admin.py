from django.contrib import admin
from crypto.models import CrptDataNews


@admin.register(CrptDataNews)
class CryptoNewsAdmin(admin.ModelAdmin):
    list_display = ['title_news']
