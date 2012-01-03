'''
Python - type and class interchangable

type means class, including the built-in types like list and int note constructor syntax: instead of [] or {}can use list() or dict()

operator mean special methond - 2 + 2 means int('2').__add__(int('2))

class is just another type, yo ucould define your own : javaclass or ...
    This is called a metaobject protocol
    
    
    
GENERATORS

Protocol = collection of methods


Created on Nov 22, 2011

@author: mark
'''

class A(object):
    def __init__(self,a):
        self.a = a

class X(object):
    def __init__(self,x,b):
        self.x = x
        self.b = b

if __name__ == '__main__':
    b = A(0)
    y = X(1,b)
    z = X(2,b)
    print b.a
    print y.x
    print y.b.a
    print z.x
    print z.b.a
    b.a = 99
    print b.a
    print y.x
    print y.b.a
    print z.x
    print z.b.a
    y.q = 7
    print y.q
    print z.q
    pass