# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 17:27:05 2018

@author: sapu.devi.dwivedi
"""
#django framework # 
#views.py
#pip install feedparser
import feedparser
from django.shortcuts import render
#rss='http://feeds.bbci.co.uk/news/rss.xml'    
def RssFeedParser(request, rss):
  feed = feedparser.parse(rss) 
  return render(request, 'rsstemplate.html', {
        'data': feed['entries'],
    }, content_type='application/xhtml+xml')
  
######################################################### 
# rsstemplate.html
<!DOCTYPE html>
<html lang="en">
<head>
  
</head>
<body>
  {% for key in data %}
  <h3>key["title"]</h3>
  <h2>key["summary"]</h2>
{% endfor %}
  
</body>
</html>    
    
    