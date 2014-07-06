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

if __name__ == '__main__':
  files = glob.glob(rawPath + '*.txt');
  dataFiles = os.listdir(dataPath);
  dataMap = {};
  for fn in dataFiles:
    dataMap[fn] = True;
  for fn in files:
    fn = os.path.basename(fn);
    print "process " + fn;
    if not(dataMap.has_key(fn)):
      print "not in data " + fn;
      f = open(rawPath + fn, "r");
      lines = f.readlines();
      if len(lines) != 4:
        print "error lines over 4 ", len(lines);
        sys.exit();
      fname = fn;
      title = lines[0].rstrip();
      user = lines[1].rstrip();
      url = lines[2].rstrip();
      desc = lines[3].rstrip();
      fw = open(dataPath + fname, "w");
      fw.write("\n".join([ fname, str(time.time()), title, user , url, desc ]));
      fw.close();
    print "==========";
  # ok

