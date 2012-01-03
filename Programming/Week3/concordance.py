'''
Created on Oct 23, 2011

@author: mark
'''
import sys


def concordance (s, source, destination):
    x = 1
    for x, line in enumerate(source) :
        if s in line :
            destination.write("Line Number : " + str(x) + "\n" + line)

if __name__ == '__main__':
    print "Enter a file to read : "
    source = str(raw_input())
    print "Enter a file to write results : "
    destination = str(raw_input())
    print "Enter a string to search for : "
    s = str(raw_input())
    try :
        sourceFile = open (source)
        destinationFile = open (destination, 'w')
    except :
        print "Error"
        sys.exit(1)
    concordance (s, sourceFile, destinationFile)
    sourceFile.close()
    destinationFile.close()
    print "DONE!"