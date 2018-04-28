'''
Functions correspond to tables 6 to 9 in JoBimText Creation process
5. Frequency significance measure: significance_le_cf_stanford(...)
6. Pruning: done when aggregating
7. Aggregating per feature: aggregate_per_feature(...)
8. Similarity Count: similarity_count(...)

Author: Ramkishore Saravanan
Computational Linguistics II - Assignment 3:
Distributional thesaurus
'''

def significance_le_cf_stanford(func, elements, context, bims):
    '''Step 6'''
    significance = {}
    highest = 0
    for bim in bims:

        # create corresponding contexts and words
        # much more efficient than searching elements and contexts dict
        c1 = ("@", bim[1], bim[2])
        c2 = (bim[0], bim[1], "@")
        w1 = bim[0]
        w2 = bim[2]

        # calculate significance scores using the func passed in params
        if not w1 in significance:
            significance[w1] = {}
        if not c1 in significance[w1]:
            significance[w1][c1] = func(elements[w1], context[c1], bims[bim])

        if not w2 in significance:
            significance[w2] = {}
        if not c2 in significance[w2]:
            significance[w2][c2] = func(elements[w2], context[c2], bims[bim])

    return significance

def aggregate_per_feature(significance, elements, context, pruning_limit):
    '''Step 7 and 8'''
    agg_per_feature = {}

    # aggregating language elements by the contexts they occur in
    for c in context:
        agg_per_feature[c] = []
        for w in elements:
            if c in significance[w]:
                # pruning is applied, note that pruning limit will depend on the function
                # used in significance_le_ce_stanford
                # different functions return values in different ranges
                if significance[w][c] > pruning_limit:
                    agg_per_feature[c].append(w)

    return agg_per_feature

def similarity_count(agg_per_feature, elements, context):
    '''Step 9'''
    similarity_count = {}

    for c in agg_per_feature:
        array = agg_per_feature[c]
        for w1 in array:
            for w2 in array:
                if w1 != w2 and w1 in array and w2 in array:
                    if not w1 in similarity_count:
                        similarity_count[w1] = {}
                    if not w2 in similarity_count[w1]:
                        similarity_count[w1][w2] = 1
                    else:
                        similarity_count[w1][w2] += 1

    return similarity_count
