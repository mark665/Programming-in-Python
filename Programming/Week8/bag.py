'''
Exercise: Write a module bag.py that defines a class named bag.  A bag (also
called a multiset) is a collection without order (like a set) but with
repetition (unlike a set) --- an element can appear one or more times
in a bag.  Implement bag as a subclass of dictionary where each bag
element is a key and its value is an integer that represents its
multiplicity (the number of repetitions).  For example in b1 =
bag({'a':2, 'b':3}), b1 is a bag where 'a' occurs twice (has
multiplicity 2) and 'b' occurs three times.  Provide a bag union
operator + (plus sign) that operates on two bags and returns a third
bag, their union.  The bag union contains all of the elements of both
bags, with their multiplicities added.  For example, after b2 =
bag({'b':1, 'c':2}), then b1 + b2 == bag({'a':2, 'b':4', 'c':2})

Created on Nov 22, 2011

@author: mark
'''
import copy

class bag(dict):
    
    def __add__ (self, otherBag):     
        newBag = copy.deepcopy(self)
        for x in otherBag : 
            if x not in newBag:
                newBag[x] = otherBag[x]
            else:
                newBag[x] += otherBag[x]
        return newBag
    
'''
       newBag = {}
        for x in set(self) + set(otherBag) :
            newBag[x] = self.get(x,0) + otherBag.get(x,0)
        return newBag
'''
    
if __name__ == '__main__':
    b2 = bag({'b':1, 'c':2})
    b1 = bag({'a':2, 'b':3})
    b3 = bag()
    b4 = bag({(1,2):1, 'what':3, 2:3, 'zero':0})
    b5 = bag({'zero':3})
    r1 = b2 + b1 + b3 + b4 + b5
    print r1
    pass