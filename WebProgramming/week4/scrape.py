'''
Created on Feb 7, 2012

@author: mark
'''
from pprint import pprint
import re, urllib2, sys

url = sys.argv[1]
result = urllib2.urlopen("http://jon-jacky.github.com/uw_python/winter_2012/index.html").read ()
pprint (re.findall('http://.*html',result))