from django.conf.urls.defaults import *
from django.conf import settings
from news_sitemaps import NewsSitemap

sitemaps = {}

if 'stories' in settings.INSTALLED_APPS:
    from stories.models import Story

    class StorySitemap(NewsSitemap):
        limit = 5000
        def items(self):
            return Story.published.all()
            
        def lastmod(self, obj):
            return obj.publish_date
    
    sitemaps['stories'] = StorySitemap
    
if 'django.contrib.flatpages' in settings.INSTALLED_APPS:
    from django.contrib.flatpages.models import FlatPage
    from django.contrib.sites.models import Site
    
    class FlatPageSitemap(NewsSitemap):
        limit = 5000
        def items(self):
            return FlatPage.objects.all()
            
    sitemaps['flatpages'] = FlatPageSitemap

urlpatterns = patterns('news_sitemaps.views',
    (r'^index\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^(?P<section>.+)\.xml', 'news_sitemap', {'sitemaps': sitemaps}),
)