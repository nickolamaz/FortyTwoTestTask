from django.contrib import admin
from apps.t3_middleware.models import HttpRequestStore


admin.site.register(HttpRequestStore)
