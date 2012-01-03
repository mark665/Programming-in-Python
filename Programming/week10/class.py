'''
Created on Dec 6, 2011

@author: mark
'''

class D(dict):
    
    def __repr__(self):
        return 'D(%s)' % dict.__repr__(self)

class X(object):
    def __init__(self,d):
        assert isinstance(d,dict)
        self.d = d
    def __repr__(self):
        return 'X(%s)' % dict.__repr__(self)


if __name__ == '__main__':
    d0 = {'a':1, 'b':2}
    d,x = D(d0), X(d0)
    for c in d: print c
    for c in x.d: print c
    dir(d)
    dir(x)
    pass    