#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Wallace'
SITENAME = 'GTmanfred'
SITEURL = ''

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.utf8'

THEME = "/home/pelican/pelican-themes/bootstrap2"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Git Repositories', 'http://code.gtmanfred.com/'),
          ('Feeds', '/feeds/'),
          ('About', '/about.html'),
          ('KaiSforza\'s Blag', 'http://kaictl.net'),
          )
EXTRA_PATH_METADATA={ 'extra/robots.txt': {'path': 'robots.txt'},}

DEFAULT_PAGINATION = 10
MARKUP = ('mkd', )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
