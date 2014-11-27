#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sheldon Kreger'
SITENAME = u'sheldonkreger'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Theme
THEME = "/Users/Skregerx/python-dev/pelican-bootstrap3"
BOOTSTRAP_THEME = 'yeti'

#Google Analytics
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-24290960-5'

# Blogroll
LINKS = (('ProDrumBlog', 'http://prodrumblog.com'),
         ('Personality Development', 'http://personality-development.org'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/profile/view?id=108829656'),
          ('Twitter', 'https://twitter.com/sheldonkreger'),
          ('Google Plus', 'https://plus.google.com/u/0/+SheldonKreger/posts'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#GitHub Pages CNAME Custom Domain Name
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
