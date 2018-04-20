from significance_measures import pmi

def significance_le_cf_stanford(func, elements, context, bims):
    significance = {}
    for bim in bims:
        c1 = ("@", bim[1], bim[2])
        c2 = (bim[0], bim[1], "@")

        w1 = bim[0]
        w2 = bim[2]

        if not w1 in significance:
            significance[w1] = {}
        if not c1 in significance[w1]:
            significance[w1][c1] = pmi(elements[w1], context[c1], bims[bim])

        if not w2 in significance:
            significance[w2] = {}
        if not c2 in significance[w2]:
            significance[w2][c2] = pmi(elements[w2], context[c2], bims[bim])

    return significance
