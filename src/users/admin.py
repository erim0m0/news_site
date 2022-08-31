from django.contrib import admin
from .models import User, IpAddress


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['last_login', 'date_joined']


admin.site.register(User, UserAdmin)
admin.site.register(IpAddress)
