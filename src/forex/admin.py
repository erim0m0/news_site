from django.contrib import admin
from forex.models import ForexData


@admin.register(ForexData)
class ForexAdmin(admin.ModelAdmin):
    list_display = ('price_name', 'price')
