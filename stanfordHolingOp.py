'''
author: Ramkishore S
Computational Linguistics II - Assignment 3:
Distributional thesaurus
Part 1: Holing Operation on stanford dependency parser output
'''

# le = language element
# cf = context feature

from nltk.parse.stanford import StanfordDependencyParser as SDP
parser = SDP()


# Arguments: corpus, an array of sentences.
def stanford_le_ce(corpus):
    context = {}
    elements = {}
    bims = {}

    for sentence in corpus:
        result = parser.raw_parse(sentence)
        dep = result.next()
        
        for dependency in list(dep.triples()):
            
            # for le, cf pairs
            
            if not dependency in bims:
                bims[dependency] = 1.
            else:
                bims[dependency] += 1

            # for cf
            
            c1 = ("@", dependency[1], dependency[2])
            if not c1 in context:
                context[c1] = 1.
            else:
                context[c1] += 1

            c2 = (dependency[0], dependency[1], "@")
            if not c2 in context:
                context[c2] = 1.
            else:
                context[c2] += 1

            # for le
            
            w1 = dependency[0]
            w2 = dependency[2]

            if not w1 in elements:
                elements[w1] = 1.
            else:
                elements[w1] += 1

            if not w2 in elements:
                elements[w2] = 1.
            else:
                elements[w2] += 1

    return context, elements, bims


if __name__ == "__main__":
    corpus = ["I saw an elephant by the blue river .",
          "We saw the elephant ."]

    context, elements, bims = stanford_le_ce(corpus)

    print ""
    for i in context:
        print i, context[i]
    print ""
    for i in elements:
        print i, elements[i]

    print ""
    for i in bims:
        print i, bims[i]
