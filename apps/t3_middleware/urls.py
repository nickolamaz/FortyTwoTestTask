from django.conf.urls import patterns, url
from apps.t3_middleware import views

urlpatterns = patterns(
    '',
    url(r'^$', views.request, name='request'),
    url(r'getrequests/$', views.requests_get, name='requests_get')
)
