'''
author: Ramkishore S
Computational Linguistics II - Assignment 3:
Distributional thesaurus
'''

from stanfordHolingOp import stanford_le_ce as context_element_loader_from
from significance_measures import pmi, ll, lmi, freq
from dt_functions import significance_le_cf_stanford

def create_distributional_thesaurus(corpus,
                                    pruning=0):
    context, elements, bims = context_element_loader_from(corpus)

    # 1. pmi can be replaced with any other similarity measure
    # 2. pmi performs better on smaller corpus
    # 3. significance_le_cf_stanford is specifically built for stanford output and
    #    might not run on trigram holing etc.
    significance = significance_le_cf_stanford(func=pmi,
                                               elements=elements,
                                               context=context,
                                               bims=bims)

    # add pruning later, for pmi highest is 0.0

if __name__ == "__main__":
    corpus = ["I saw an elephant in the park",
              "We saw a lion eat an elephant",
              "It is in the park we saw a lion"]
    create_distributional_thesaurus(corpus)
