from django.conf.urls import patterns, url
from apps.t3_middleware import views

urlpatterns = patterns(
    '',
    url(r'^$', views.requests_view, name='request'),
)
