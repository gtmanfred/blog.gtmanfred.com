#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Wallace'
SITENAME = 'GTmanfred'
SITEURL = 'http://blog.gtmanfred.com'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.utf8'

THEME = "themes/pelican-bootstrap3"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Git Repositories', 'http://code.gtmanfred.com/'),
          ('Feeds', '/feeds/'),
          ('KaiSforza\'s Blag', 'http://kaictl.net'),
          )
EXTRA_PATH_METADATA={ 'extra/robots.txt': {'path': 'robots.txt'},}

DEFAULT_PAGINATION = 10
MARKUP = ('mkd', )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "gtmanfred"
GOOGLE_ANALYTICS = "UA-42514099-1"
