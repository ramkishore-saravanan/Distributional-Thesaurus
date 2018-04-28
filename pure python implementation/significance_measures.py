'''
Similarity measures used in JoBim text
Only pmi and npmi are implemented 
othes are to be implemented

Author: Ramkishore Saravanan
Computational Linguistics II - Assignment 3:
Distributional thesaurus
'''

from math import log

def pmi(p_x, p_y, p_x_y):
    '''Point wise Mutual Information'''
    try:
        return log(p_x_y/(p_x * p_y))
    except ZeroDivisionError:
        return -1

def npmi(p_x, p_y, p_x_y):
    '''Normalized pointwise mutual information'''
    try:
        return log(p_x_y/(p_x * p_y))/(-log(p_x_y) + 0.000000001)
    except ZeroDivisionError:
        return -1

def ll():
    pass

def lmi():
    pass

def freq():
    pass

if __name__ == "__main__":
    assert(pmi(2., 1., 1.) == log(1./2.))