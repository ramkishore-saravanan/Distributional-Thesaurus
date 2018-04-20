'''
Similarity measures used in JoBim text
I use only pmi, othes are to be implemented
'''

from math import log

def pmi(p_x, p_y, p_x_y):
    try:
        return log(p_x_y/(p_x * p_y))
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
