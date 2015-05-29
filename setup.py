import os
from setuptools import setup, find_packages
import news_sitemaps

try:
    long_description = open('README.rst').read()
except IOError:
    long_description = ''

try:
    reqs = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read()
except (IOError, OSError):
    reqs = ''

setup(
    name='django-news-sitemaps',
    version=news_sitemaps.get_version(),
    description='Generates sitemaps compatible with the Google News schema',
    author='CallowayProject',
    author_email='webdev@callowayproject.com',
    url='http://github.com/callowayproject/django-news-sitemaps/',
    include_package_data=True,
    packages=find_packages(exclude=['example']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ]
)
