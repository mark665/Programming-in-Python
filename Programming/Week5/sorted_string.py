'''
Created on Nov 1, 2011

@author: mark
'''

def sorted_string (s):
    t = []
    for c in s:
        t.append(c)
    t.sort()
    r = "".join(t)
    return r
     
    
    return

if __name__ == '__main__':
    s = "Data types. Sequences again. Tuples, Lists, Dictionaries. Mutability. Aliasing. Argument passing. List comprehensions."
    t = "A tuple is a sequence of values. The values can be any type, and they are indexed by integers, so in that respect tuples are a lot like lists. The important difference is that tuples are immutable."
    print s
    print sorted_string(s)
    print t
    print sorted_string(t)
    pass