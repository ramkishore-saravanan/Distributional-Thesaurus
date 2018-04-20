'''
author: Ramkishore S
Computational Linguistics II - Assignment 3:
Distributional thesaurus
'''

from stanfordHolingOp import stanford_le_ce as context_element_loader_from
from significance_measures import pmi, npmi, ll, lmi, freq
from dt_functions import significance_le_cf_stanford, \
    aggregate_per_feature, similarity_count

def create_distributional_thesaurus(corpus,
                                    pruning=0):
    context, elements, bims = context_element_loader_from(corpus)

    # 1. pmi can be replaced with any other similarity measure
    # 2. pmi performs better on smaller corpus
    # 3. significance_le_cf_stanford is specifically built for stanford output and
    #    might not run on trigram holing etc.
    # 4. consider using normalised pmi = npmi
    significance = significance_le_cf_stanford(func=pmi,
                                               elements=elements,
                                               context=context,
                                               bims=bims)

    # pruning is included in this function
    agg_per_feature = aggregate_per_feature(significance,
                                            elements,
                                            context,
                                            -10)

    sim_count = similarity_count(agg_per_feature,
                                 elements,
                                 context)

    # for i in agg_per_feature:
    #     print "context: ", i," words: ", agg_per_feature[i]
    # print ""
    for i in sim_count:
        for j in sim_count[i]:
            print i, j, sim_count[i][j]

if __name__ == "__main__":
    # dummy_corpus = ["I saw an elephant in the park .",
    #           "We saw a lion eat an elephant .",
    #           "It is in the park we saw a lion .",
    #           "I saw a lion and a elephant ."]
    # create_distributional_thesaurus(dummy_corpus)

    with open('/Users/ramkishoresaravanan/Desktop/mouse_corpus.txt') as f:
        corpus = f.read().splitlines()

    create_distributional_thesaurus(corpus)
    # for i in significance:
    #     for j in significance[i]:
    #         print i, " ", j, " ", significance[i][j]

    # print ""
