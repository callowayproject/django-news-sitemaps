Django News Sitemaps
=====================

This is an implementation of sitemaps with news specific tags as defined by `Google's News Sitemaps <http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=74288>`_ specification.
It is just regular Django sitemaps with a couple other tags added in specifically for news publications.

Install
--------

For starters, just place ``news_sitemaps`` into your ``INSTALLED_APPS`` and then you can load the default urlconf like so::

    urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
        ...
        (r'^news-sitemaps/', include('news_sitemaps.urls')),
    )

This will create a ``/news-sitemaps/index.xml`` which is a sitemap index of all available sitemaps which will appear by section at urls like ``/news-sitemaps/<section>.xml`` (more on this later)


Settings
---------

Three new settings are defined to control content of your news sitemaps


PUBLICATION_NAME
^^^^^^^^^^^^^^^^

The proper name of the news publication.
It must exactly match the name as it appears on your articles in news.google.com, omitting any trailing parentheticals.
By default it is "The Example Times" so please set this.


PUBLICATION_LANGUAGE
^^^^^^^^^^^^^^^^^^^^

The language code of your publication. It should be an ISO 639 Language Code (either 2 or 3 letters).
Defaults to Django's ``LANGUAGE_CODE`` setting.


PUBLICATION_TIME_ZONE
^^^^^^^^^^^^^^^^^^^^^

The timezone suffix for your news publication. Defaults to "-5:00" (America/Eastern)


Adding Sitemaps
----------------

To add your own news sitemaps you must register them with the app first.
Here is a quick and dirty example of creating a news sitemap for Django's Comments::

    from news_sitemaps import register, NewsSitemap
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
    
Then the comments sitemap will appear on your index sitemap and you will be able to access
the actual sitemap at /news-sitemaps/comments.xml.

Notice the ``genres`` method. There are a few new methods in addition to the normal Sitemap methods which are news specific.
They are: ``title``, ``access``, ``keywords``, ``stock_tickers``, and ``genres``.
Please refer to `Google's News Sitemaps <http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=74288>`_ specification for more info on how to use them correctly.