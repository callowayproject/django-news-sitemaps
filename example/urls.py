from django.conf.urls.defaults import *
from news_sitemaps.urls import urlpatterns as sitemap_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
) + sitemap_patterns

