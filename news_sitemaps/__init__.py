from django.conf import settings
from sitemaps import NewsSitemap

registry = {}

def register(**kwargs):
    for name,sitemap in kwargs.items():
        registry[name] = sitemap
    

if 'stories' in settings.INSTALLED_APPS:
    from stories.models import Story

    class StorySitemap(NewsSitemap):
        limit = 5000
        def items(self):
            return Story.published.all()
            
        def lastmod(self, obj):
            return obj.publish_date
    
    register(stories=StorySitemap)
