from django.contrib import admin
from .models import Notification


# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'is_active', 'create_by']
    list_editable = ['is_active']

    def save_model(self, request, obj, form, change):
        obj.create_by = request.user
        return super(NotificationAdmin, self).save_model(request, obj, form, change)


admin.site.register(Notification, NotificationAdmin)
