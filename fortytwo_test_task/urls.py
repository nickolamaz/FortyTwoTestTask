from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
import views
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/', views.request, name='request'),
    # url(r'^login/$', 'django.contrib.auth.views.login',
    #     {"template_name": "login.html"}),
    # url(r'^logout/', views.logout, name='logout'),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='login'),
    url(r'^accounts/register/', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/'), name='register'),
    url(r'^edit/', views.edit, name='edit'),
)
