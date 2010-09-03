from django.conf.urls.defaults import *
from django.conf import settings

from news_sitemaps import registry


urlpatterns = patterns('news_sitemaps.views',
    (r'^index\.xml$', 'index', {'sitemaps': registry}),
    (r'^(?P<section>.+)\.xml', 'news_sitemap', {'sitemaps': registry}),
)