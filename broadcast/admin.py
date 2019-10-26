from django.contrib import admin
from .models import *


class BroadcastAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['name', ('url', 'is_active'), ('created', 'updated')]
    list_display = ['name', 'url', 'is_active', 'created']
    list_filter = ['name']

    class Meta:
        model = Broadcast


admin.site.register(Broadcast, BroadcastAdmin)