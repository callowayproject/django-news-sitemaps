import datetime
from django.contrib.sitemaps import Sitemap

class NewsSitemap(Sitemap):
    def genres(self, obj):
        """
        Returns a comma-separated list of properties characterizing the content of the article,
        such as "PressRelease" or "UserGenerated." Your content must be labeled accurately,
        in order to provide a consistent experience for our users.
        
        Options are::
        
            * PressRelease (default, visible): an official press release.
            * Satire (visible): an article which ridicules its subject for didactic purposes.
            * Blog (visible): any article published on a blog, or in a blog format.
            * OpEd: an opinion-based article which comes specifically from the Op-Ed section of your site.
            * Opinion: any other opinion-based article not appearing on an Op-Ed page, i.e., reviews, interviews, etc.
            * UserGenerated: newsworthy user-generated content which has already gone through a formal editorial review process on your site.
        """
        return 'PressRelease'
    
    def title(self, obj):
        """
        Returns the title of the news article.
        Note: The title may be truncated for space reasons when shown on Google News.
        """
        if hasattr(obj, 'title'):
            return obj.title
        elif hasattr(obj, 'name'):
            return obj.name
        elif hasattr(obj, 'headline'):
            return obj.headline
    
    def keywords(self, obj):
        """
        Returns a comma-separated list of keywords describing the topic of the article.
        Keywords may be drawn from, but are not limited to, the list of existing Google News keywords.
        """
        if hasattr(obj, 'keywords'):
            return obj.keywords
        elif hasattr(obj, 'tags'):
            return obj.tags
    
    def access(self, obj):
        """
        Returns description of the accessibility of the article.
        If the article is accessible to Google News readers without a registration or subscription,
        this function should return None
        
        Options are::
        
            * Subscription (visible): an article which prompts users to pay to view content.
            * Registration (visible): an article which prompts users to sign up for an unpaid account to view content.
        """
    
    def stock_tickers(self, obj):
        """
        Returns a comma-separated list of up to 5 stock tickers of the companies,
        mutual funds, or other financial entities that are the main subject of the article.
        Relevant primarily for business articles.
        Each ticker must be prefixed by the name of its stock exchange,
        and must match its entry in Google Finance.
        For example, "NASDAQ:AMAT" (but not "NASD:AMAT"), or "BOM:500325" (but not "BOM:RIL").
        """
    
    def get_urls(self, page=1):
        from django.contrib.sites.models import Site
        domain = Site.objects.get_current().domain
        get = self._Sitemap__get

        for item in self.paginator.page(page).object_list:
            lastmod = get('lastmod', item, None)
            if isinstance(lastmod, datetime.time) or isinstance(lastmod, datetime.datetime):
                lastmod = lastmod.replace(microsecond=0)

            yield {
                'location':     "http://%s%s" % (domain, get('location', item)),
                'lastmod':      lastmod,
                'changefreq':   get('changefreq', item, None),
                'priority':     get('priority', item, None),
                
                # News attrs
                'title':        get('title', item, None),
                'access':       get('access', item, None),
                'keywords':     get('keywords', item, None),
                'genres':       get('genres', item, None),
                'stock_tickers':get('stock_tickers', item, None),
            }
