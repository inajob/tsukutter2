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

  fhead = open(headerHtml, "r");
  headerStr = fhead.read();
  fhead.close();

  ffoot = open(footerHtml, "r");
  footerStr = ffoot.read();
  ffoot.close();
 
  fh.write(headerStr);
  for x in out:
    fh.write('- <a target="_blank" href="' + html(x['url']) + '">' + html(x['title']) + '</a> by ' + html(x['user']) + ' ' + html(x['desc']) +'<br>\n');

  fh.write(footerStr);
  fh.close();
    
  print "== done dump html =="

