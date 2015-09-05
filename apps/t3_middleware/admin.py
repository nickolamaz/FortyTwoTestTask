from django.contrib import admin
from apps.t3_middleware.models import HttpRequestStore


class HttpRequestStoreAdmin(admin.ModelAdmin):
    list_display = ('date', 'method', 'path', 'host', 'priority')
    list_filter = ['priority']

admin.site.register(HttpRequestStore, HttpRequestStoreAdmin)
