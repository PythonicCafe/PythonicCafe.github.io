#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import glob
import json

AUTHOR = 'Marcel Marques'
SITENAME = 'Pythonic.cafe'
SITEURL = ''

PATH = 'content'
THEME = 'theme'

TIMEZONE = "America/Sao_Paulo"

DEFAULT_LANG = "pt-br"

LOCALE = "pt_BR.UTF-8"

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Configurações da página de comunidades locais
VIDEOS = [
    json.load(open(fname, 'r', encoding='utf-8'))
    for fname in glob.glob('content/videos/*.json')
]

# Texts
VIDEOS_DESCRIPTION = (
    'Esses são alguns dos vídeos produzidos em nosso projeto.'
    ' Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
    ' Ut vel repudiandae voluptates tempore iusto architecto enim'
    ' similique quasi aut, debitis sed repellendus, commodi natus'
    ' animi ipsam minus temporibus libero laborum.'
)
COURSES_TEXT = (
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
    ' Ut vel repudiandae voluptates tempore iusto architecto enim'
    ' similique quasi aut, debitis sed repellendus, commodi natus'
    ' animi ipsam minus temporibus libero laborum.'
)
