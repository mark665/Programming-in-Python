'''
Created on Oct 27, 2011

@author: mark
'''

l = [1,2]
l.sort()
"""list.sort Found at: __builtin__
L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN 
 PLACE*;
    cmp(x, y) -> -1, 0, 1"""

s1 = [1,2,3]
s2 = s1
s2
s2 == s1
s2 is s1
id(s2)
id(s1)
s1[1] = 99
s1
s2
s2[2]  = 999
s2
s1

def f(i,s): i = 42; s[1] = 42

x = 99
s = [1,2,3]
f(x,s)
x
s

