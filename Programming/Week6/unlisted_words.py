'''
Created on Nov 8, 2011

@author: mark
'''
import re

def words(text): return re.findall('[a-z]+', text.lower())

def unlisted_words (sample, referance):
    s = set(words(sample))
    r = set(words (referance))
    return list(s - r)


if __name__ == '__main__':
    referance = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    sample = "this is a test a b a b c d e f g h i j k l m n o p q r s t u v w x y z ;'!#@$%^124 12345:#@$%"
    print unlisted_words(sample, referance)
    
    sampleFile = open ("big.txt")
    sample = file.read(sampleFile)
    referanceFile = open ("words.txt")
    referance = file.read(referanceFile)
    print unlisted_words(sample, referance)
