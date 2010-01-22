from distutils.core import setup

setup(
    name = 'news_sitemaps',
    version="0.1",
    description = 'Generates sitemaps compatible with the Google News schema',
    author = 'TWT Web Devs',
    author_email = 'webdev@washingtontimes.com',
    url = 'http://opensource.washingtontimes.com/projects/django-news-sitemaps/',
    packages = ['news_sitemaps'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ]
)
