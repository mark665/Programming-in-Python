#Mark Price
#Learning Python
#Fall 2011
"""
This script prompts the user for an integer, and draws a grid
the size (nxn) specified by the user
"""


def isEven (n):
#Returns true if even false if odd
    if n%2 == 0 :
        return True
    else :
        return False

def printLineAGrid (size):
    line = '+'
    if isEven(size) :
        modifier=(size/2)-2
        line = line + '-'*modifier + '++' + '-'*modifier + '+'
    else :
        modifier=(size/2)-1
        line = line + '-'*modifier + '+' + '-'*modifier + '+'
    return line
    
def printLineBGrid (size):
    line = '+'
    if isEven(size) :
        modifier=(size/2)-2
        line = line + ' '*modifier + '++' + ' '*modifier + '+'
    else :
        modifier=(size/2)-1
        line = line + ' '*modifier + '+' + ' '*modifier + '+'
    return line

def printGrid (size):
    #special case 1x1 and 2x2 grids
    if size == 1 :
        print '+'
        return
    if size == 2 :
        print "++\n++"
        return
    print printLineAGrid (size)
    #if even, draw use two lines/columns for "grid"
    if isEven(size) :
        for x in range((size/2)-2) :
            print printLineBGrid (size)
        print printLineAGrid (size)
        print printLineAGrid (size)
        for x in range((size/2)-2) :
            print printLineBGrid (size)         
    #if odd, use "normal" looking grid
    else :
        for x in range((size/2)-1) :
            print printLineBGrid (size)
        print printLineAGrid (size)
        for x in range((size/2)-1) :
            print printLineBGrid (size)
    print printLineAGrid (size)
    

gridSize = -1
while gridSize != 0 : 
    while gridSize < 1 :
        print "Enter Grid Size, 0 to exit : \n"
        gridSize = int(raw_input())
    printGrid (gridSize)
    gridSize = -1