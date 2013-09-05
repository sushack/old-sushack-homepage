from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .views import Home, SignUp


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^signup/$', SignUp.as_view(), name='signup'),
    url(r'^admin/', include(admin.site.urls)),
)

