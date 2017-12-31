#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
CWD = os.getcwd()

AUTHOR = u'Sheldon Kreger'
SITENAME = u'sheldonkreger'
SITEURL = ''
PATH = CWD + '/content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

# About
# AVATAR = 'images/sheldonkreger.jpg'
ABOUT_ME = 'Web engineer, athlete, musician, lover.'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Theme
THEME = "/home/sheldonkreger/pelican-themes/pelican-blueidea"
#BOOTSTRAP_THEME = 'yeti'

#Twitter
TWITTER_USERNAME = 'sheldonkreger'
TWITTER_CARDS = 'true'

#Google Analytics
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-24290960-5'

# Blogroll
LINKS = (('ProDrumBlog', 'http://prodrumblog.com'),
         ('Personality Development', 'http://personality-development.org'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/profile/view?id=108829656'),
          ('Twitter', 'https://twitter.com/sheldonkreger'),
          ('Google Plus', 'https://plus.google.com/u/0/+SheldonKreger/posts'),
          ('YouTube', 'https://www.youtube.com/sheldonkreger'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ["plugins", "/home/sheldonkreger/pelican-plugins"]

#GitHub Pages CNAME Custom Domain Name
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
