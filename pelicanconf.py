#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import glob
import json
import datetime

AUTHOR = 'Marcel Marques'
SITENAME = 'Pythonic.cafe'
SITEURL = ''
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
PAGE_SAVE_AS = '{slug}.html'

PATH = 'content'
THEME = 'theme'

TIMEZONE = "America/Sao_Paulo"

DEFAULT_LANG = "pt-br"

LOCALE = "pt_BR.UTF-8"

# Links navbar and footer 
NAVBAR_LINKS = [
    {
        'title': 'Home',
        'href': 'index',
    },
    {
        'title': 'Projetos',
        'href': 'projetos',
    },
    {
        'title': 'Videos',
        'href': 'videos',
    },
    {
        'title': 'Cursos',
        'href': 'cursos',
    },
    {
        'title': 'Comunidades',
        'href': 'comunidades',
    },
    {
        'title': 'Contato',
        'href': 'contato',
    }
]

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Methods
def getContentElements(path):
    object_list = [json.load(open(fname, 'r', encoding='utf-8'))
                   for fname in glob.glob(path)]
    return object_list

def getSortedByDate(path):
    object_list = getContentElements(path)
    object_list.sort(key=lambda x: x["date"], reverse=True)
    return object_list

# Titles and texts showed in home and pages
HOME_TITLE = 'Tudo sobre o mundo Python!'
HOME_CAPTION = (
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
    ' Ut vel repudiandae voluptates tempore iusto architecto enim'
    ' similique quasi aut, debitis sed repellendus, commodi natus'
    ' animi ipsam minus temporibus libero laborum.'
)

VIDEOS = getSortedByDate('content/videos/*.json')
VIDEOS_TITLE = 'Videos'
VIDEOS_DESCRIPTION = (
    'Esses são alguns dos vídeos produzidos em nosso projeto.'
    ' Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
    ' Ut vel repudiandae voluptates tempore iusto architecto enim'
    ' similique quasi aut, debitis sed repellendus, commodi natus'
    ' animi ipsam minus temporibus libero laborum.'
)

PROJECTS = getContentElements('content/projects/*.json')
PROJECTS_CAPTION = 'CONHEÇA NOSSOS TRABALHOS'
PROJECTS_TITLE = 'Projetos desenvolvidos'

COURSES = getContentElements('content/courses/*.json')
COURSESE_CAPTION = 'CONHECIMENTO E APRENDIZADO'
COURSESE_TITLE = 'Cursos'
COURSES_TEXT = (
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
    ' Ut vel repudiandae voluptates tempore iusto architecto enim'
    ' similique quasi aut, debitis sed repellendus, commodi natus'
    ' animi ipsam minus temporibus libero laborum.'
)