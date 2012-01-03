'''
+--
 Assignment for week 7, Tues Nov 22, bring exercise to turn in (hardcopy)

 Python Tutorial: Section 9, Classes, except 9.9 - 9.11
 http://docs.python.org/tutorial/classes.html

Write a module atom.py that defines a class named Atom whose base
class is object.  An atom has a chemical symbol (a string).  An atom
can have chemical bonds to other atoms.  When an atom is created, it
has no bonds to other atoms.  Each atom can have no more than a
certain maximum number of bonds to other atoms.  When one atom has a
bond to another atom, the second atom must have a bond back to the
first.  An atom may have more than one bond to the same atom.  Every
atom has a method that returns a description string that contains its
chemical symbol, a unique identity, and the chemical symbols and
unique identities of all the atoms to which it has bonds.  The
identity in this string must be different in every atom, and must
always be the same in a given atom.

The atom module defines two more classes that represent hydrogen and
oxygen atoms, each with the base class Atom.  Every hydrogen atom has
the chemical symbol 'H' and has at most one bond.  Every oxygen atom
has the chemical symbol 'O' and has at most two bonds.

Also in atom.py, write code that tests the atom classes.  This test
code should execute only when the module is executed at top level, not
when it is imported.  This test code creates three hydrogen atoms and
two oxygen atoms.  Then this code creates bonds between one of the
oxygens and two of the hydrogens (forming a water molecule).  Then it
prints the description string of every atom.

Hints and reminders:
 This shouldn't take more than a page or two of code
 Use class attributes for data common to all instances of a class
 Instance attributes can be lists, you can have lists of objects
 Turn in what you have on Nov 22, even if it is not finished
 
Created on Nov 15, 2011

@author: mark
'''

import copy, sys

class Atom (object):
    """
    Atom base calss for all elemnts
    """
    maxbonds = sys.maxint
    
    def __init__(self, symbol = "H"  , bonds = []) :
        if len(bonds) < self.maxbonds :
            self.symbol = symbol
            for b in bonds :
                self.createBond(b)
        else :
            return 1
    
    def __str__(self):
        bondString = ""
        local = str(self.symbol)+ " " + str(id(self)) + " "
        if self.bonds : 
            bondString = [str(x.symbol)+ " " + str(id(x)) + " " for x in self.bonds]
        return local + str(bondString)
    
    def createBond (self, target):
        if (len(self.bonds) < self.maxbonds and len(target.bonds) < target.maxbonds) :
            self.bonds.append(target)
            target.bonds.append(self)
        else :
            return 1
        

class Oxygen (Atom):

    maxbonds = 2
    symbol = 'O'
    
    def __init__(self, symbol = "O", bonds = []) :
        if len(bonds) < self.maxbonds :
            self.bonds = copy.deepcopy(bonds)
            for b in bonds :
                self.createBond(b)            
        else :
            return 1
    
class Hydrogen (Atom):
    
    maxbonds = 1
    symbol = 'H'
    
    def __init__(self, symbol = "H", bonds = []) :
        if len(bonds) < self.maxbonds :
            self.bonds = copy.deepcopy(bonds)
            for b in bonds :
                self.createBond(b)
        else :
            return 1

if __name__ == '__main__':
    hydrogen = Hydrogen()
    oxygen1 = Oxygen()
    oxygen2 = Oxygen()
    
    l = [hydrogen,oxygen1,oxygen2]
    for x in l :
        print x 
    oxygen1.createBond(hydrogen)
    oxygen2.createBond(hydrogen)
    hydrogen2 = Hydrogen()
    hydrogen3 = Hydrogen(bonds = [oxygen1, oxygen2, hydrogen])
    hydrogen3 = Hydrogen()
    hydrogen2.createBond(oxygen1)
    l = [hydrogen, hydrogen2, hydrogen3, oxygen1,oxygen2]
    for x in l :
        print x