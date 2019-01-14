#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Wallace'
SITENAME = 'GTmanfred'
SITEURL = 'https://blog.gtmanfred.com'
SITELOGO = SITEURL + '/images/profile.png'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.utf8'

THEME = "themes/flex"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'post_stats']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll

STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/keybase.txt': {'path': 'keybase.txt'},
    'extras/custom.css': {'path': 'static/custom.css'},
}
DEFAULT_PAGINATION = 10
MARKUP = ('mkd', )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "gtmanfred"
GOOGLE_ANALYTICS = "UA-42514099-1"

BROWSER_COLOR = '#333'

SOCIAL = (('linkedin', 'https://br.linkedin.com/in/danielwallace90/en'),
          ('github', 'https://github.com/gtmanfred'),
          ('twitter', 'https://twitter.com/gtmanfred'),
          ('reddit', 'https://reddit.com/u/gtmanfred'),
          ('rss', '/feeds/all.atom.xml'))

MAIN_MENU = True
