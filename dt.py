'''
author: Ramkishore S
Computational Linguistics II - Assignment 3:
Distributional thesaurus
'''

from stanfordHolingOp import stanford_le_ce as context_element_loader_from

# load corpus
corpus = []

context, elements, bims = context_element_loader_from(corpus)
