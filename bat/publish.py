#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import datetime
import re
import time;
import os;
import glob;
import sys;
import logging

rawPath = '../raw_data/';
dataPath = '../data/'
outFile = '../current.json'
outHtml = '../index.html'
outRss = '../index.xml'
headerHtml = '../parts/header.html'
footerHtml = '../parts/footer.html'

def html(text):
    text = text.replace('&', '&amp;')
    text = text.replace('"', '&quot;')
    text = text.replace("'", '&#39;')
    text = text.replace(">", '&gt;')
    text = text.replace("<", '&lt;')
    return text

if __name__ == '__main__':
  files = glob.glob(dataPath + '*.txt');
  out = [];
  for fn in files:
    print "fname: " + fn
    f = open(fn, "r");
    lines = f.readlines();
    if len(lines) != 6:
      print "error lines over 6 ", len(lines);
      sys.exit();
    fname = fn;
    ptime = lines[1].rstrip();
    title = lines[2].rstrip();
    user = lines[3].rstrip();
    url = lines[4].rstrip();
    desc = lines[5].rstrip();
    out.append({
      "time": ptime,
      "title": title,
      "user": user,
      "url": url,
      "desc": desc
    });
    f.close();
    print "==========";
  # ok
  fw = open(outFile, "w");
  fw.write(json.dumps(out));
  fw.close();
  print "== done dump json =="
  fh = open(outHtml, "w");

  fr = open(outRss, "w");
  fr.write("""<?xml version='1.0' encoding='UTF-8'?>
<rss version='2.0'>
<channel>
<title>tsukutter2</title>
<link>http://inajob.github.io/tsukutter2/index.html</link>
<description>tsukutter2</description>
""");
  for x in out:
    fr.write('<item><title>'+ html(x['title']) +'</title><link>'+ html(x['url']) +'</link><description>'+ html(x['desc']) +'</description><pubDate>'+ datetime.datetime.fromtimestamp(float(ptime)).strftime("%a, %d %b %Y %H:%M:%S %z") +'</pubDate></item>');
  fr.write("""
</channel>
</rss>""");
 
  fr.close();
  print "== done dump rss =="
  fr = open(outHtml, "w");



  fhead = open(headerHtml, "r");
  headerStr = fhead.read();
  fhead.close();

  ffoot = open(footerHtml, "r");
  footerStr = ffoot.read();
  ffoot.close();
 
  fh.write(headerStr);
  for x in out:
    fh.write('- <a target="_blank" href="' + html(x['url']) + '">' + html(x['title']) + '</a>' + '<a target="_blank" href="http://b.hatena.ne.jp/entry/' + html(x['url']) + '"><img src="http://b.hatena.ne.jp/entry/image/'+ html(x['url']) +'"></a>' + ' by ' + html(x['user']) + ' ' + html(x['desc']) +'<br>\n');

  fh.write(footerStr);
  fh.close();
    
  print "== done dump html =="

