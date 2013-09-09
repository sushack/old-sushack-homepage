from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

from .views import Home


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)
