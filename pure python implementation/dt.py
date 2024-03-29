'''
Author: Ramkishore Saravanan
Computational Linguistics II - Assignment 3:
Distributional thesaurus

Creating Distributional thesaurus using JoBimText
'''

from stanfordHolingOp import stanford_le_ce as context_element_loader_from, holingOp
from significance_measures import pmi, npmi, ll, lmi, freq
from dt_functions import significance_le_cf_stanford, \
    aggregate_per_feature, similarity_count

# ----------------- Parsed data of mouse corpus --------------------

from parsed.output import sentence as parserOutput1
from parsed.output2 import sentence as parserOutput2
from parsed.output3 import sentence as parserOutput3
from parsed.output4 import sentence as parserOutput4
from parsed.output5 import sentence as parserOutput5

# ==================================================================

def create_distributional_thesaurus(corpus=None,
                                    pruning=-10,
                                    min_sim_count=3):
    ''' creating JoBimText thesaurus '''
    # Steps 1 to 5 in JoBimText creation process
    # if no corpus is passed, mouse corpus's parsed data is used
    if not corpus:
        parserOutput1.extend(parserOutput2)
        parserOutput1.extend(parserOutput3)
        parserOutput1.extend(parserOutput4)
        parserOutput1.extend(parserOutput5)
        context, elements, bims = holingOp(parserOutput1)
    else:
        context, elements, bims = context_element_loader_from(corpus)

    # Step 6:
    # 1. pmi can be replaced with any other similarity measure
    # 2. pmi performs better on smaller corpus
    # 3. significance_le_cf_stanford is specifically built for stanford output and
    #    might not run on trigram holing etc.
    # 4. consider using normalised pmi = npmi
    significance = significance_le_cf_stanford(func=pmi,
                                               elements=elements,
                                               context=context,
                                               bims=bims)
    # Step 7 & 8:
    # pruning is included in this function
    agg_per_feature = aggregate_per_feature(significance,
                                            elements,
                                            context,
                                            pruning)

    # Step 9:
    # similarity count for aggregated data.
    sim_count = similarity_count(agg_per_feature,
                                 elements,
                                 context)

    # ---------------------- create a python file with the thesaurus ----------------------

    print ""
    # for i in agg_per_feature:
    #     print "context: ", i," words: ", agg_per_feature[i]
    # print ""

    print "distributional_thesaurus = ["
    for i in sim_count:
        for j in sim_count[i]:
            if sim_count[i][j] > min_sim_count:
                print "[", i, ",", j, ",", sim_count[i][j], "],"
    print "]"

    print ""
    print ""

    print "elements = ", elements

    # ===================================================================================

def main(debug=True):
    ''' set debug to False '''
    if debug:
        dummy_corpus = ["I saw an elephant in the park .",
                        "We saw a lion eat an elephant .",
                        "It is in the park we saw a lion .",
                        "I saw a lion and a elephant ."]
        create_distributional_thesaurus(dummy_corpus)
    else:
        create_distributional_thesaurus()

if __name__ == "__main__":
    main(debug=False)
