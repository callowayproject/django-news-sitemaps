from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.sites.models import Site
from django.core import urlresolvers
from django.utils.encoding import smart_str
from django.core.paginator import EmptyPage, PageNotAnInteger

from settings import LANG, NAME

def news_sitemap(request, sitemaps, section=None):
    maps, urls = [], []
    if section is not None:
        if section not in sitemaps:
            raise Http404("No sitemap available for section: %r" % section)
        maps.append(sitemaps[section])
    else:
        maps = sitemaps.values()
    page = request.GET.get("p", 1)
    for site in maps:
        try:
            if callable(site):
                urls.extend(site().get_urls(page))
            else:
                urls.extend(site.get_urls(page))
        except EmptyPage:
            raise Http404("Page %s empty" % page)
        except PageNotAnInteger:
            raise Http404("No page '%s'" % page)
    xml = smart_str(loader.render_to_string('sitemaps/news_sitemap.xml', {
        'urlset': urls,
        'publication_name': NAME,
        'publication_lang': LANG,
    }))
    return HttpResponse(xml, mimetype='application/xml')
