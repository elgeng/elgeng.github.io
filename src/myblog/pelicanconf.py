#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'elgeng'
SITENAME = u'elgeng'
SITEURL = ''
THEME = 'bootstrap2'
PATH = 'content'



DEFAULT_LANG = u'zh-CN' #默认语言设置
DATE_FORMATS = {"zh-CN":("zh-CN","%Y-%m-%d,%a"),} #日期格式设置，可按自己喜好设定

TIMEZONE = 'Asia/Shanghai' #时区设置

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
