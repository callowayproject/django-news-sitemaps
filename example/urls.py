from django.conf.urls.defaults import *
from news_sitemaps import register, NewsSitemap

from django.contrib import admin
admin.autodiscover()

from django.contrib.comments.models import Comment

class CommentSitemap(NewsSitemap):
    limit = 5000
    def items(self):
        return Comment.objects.filter(is_public=True,is_removed=False)
        
    def lastmod(self, obj):
        return obj.submit_date
    
    def genres(self, obj):
        return 'UserGenerated, Opinion'
        
register(comments=CommentSitemap)


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^news-sitemaps/', include('news_sitemaps.urls')),
)

