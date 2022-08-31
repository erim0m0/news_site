from django.contrib import admin
from .models import BrsDataNews


class DataNewsAdmin(admin.ModelAdmin):
    list_display = ["title_news", "place_news"]


admin.site.register(BrsDataNews, DataNewsAdmin)
