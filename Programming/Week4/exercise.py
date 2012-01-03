'''
Created on Oct 31, 2011

@author: mark

Exercise: 12.3 in Downey - write the function most_frequent that takes a string
 and prints the letters in decreasing order of frequency. ...
'''

def histogram (s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def reverse_pairs (ts):
    sor = []
    for c, f in ts.items() :
        sor.append((f, c))
    return sor

def most_frequent (s):
    d = histogram(s)
    sor = reverse_pairs(d)
    sor.sort(reverse=True)
    for f, c in sor :
        print ("%c occurs %d times" % (c, f))    
    return sor
    

if __name__ == '__main__':
    print ("Enter your string:")
    s = raw_input()
    sor = most_frequent (s)

    pass