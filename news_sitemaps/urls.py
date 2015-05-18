from django.conf.urls import patterns, url

from news_sitemaps import registry


urlpatterns = patterns('news_sitemaps.views',
    url(r'^index\.xml$',
        'index',
        {'sitemaps': registry},
        name='news_sitemaps_index'),

    url(r'^(?P<section>.+)\.xml',
        'news_sitemap',
        {'sitemaps': registry},
        name='news_sitemaps_sitemap'),
)
