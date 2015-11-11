from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('apps.t1_base.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/', include('apps.t3_middleware.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='login'),
    url(r'^accounts/register/', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/'), name='register'),
    url(r'^edit/', include('apps.t5_form_edit.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
