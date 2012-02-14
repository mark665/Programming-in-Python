'''
Created on Feb 7, 2012

@author: mark
'''

"""
NOTES:

freebase.com - database intended for exclusive use as an api
"""

import urllib2

result = urllib2.urlopen('http://google.com').read ()
print result


if __name__ == '__main__':
    pass