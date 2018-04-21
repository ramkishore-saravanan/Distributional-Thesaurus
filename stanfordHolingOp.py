'''
author: Ramkishore S
Computational Linguistics II - Assignment 3:
Distributional thesaurus
Part 1: Holing Operation on stanford dependency parser output
'''

# le = language element
# cf = context feature

import sys
from nltk.parse.stanford import StanfordDependencyParser as SDP
parser = SDP()
count = 0

def dict_update(token, dic):
    if not token in dic:
        dic[token] = 1.
    else:
        dic[token] += 1

# Arguments: corpus, an array of sentences.
# Applies holing op and returns appropriate vars
def stanford_le_ce(corpus):
    global count
    context = {}
    elements = {}
    bims = {}

    for sentence in corpus:
        result = parser.raw_parse(sentence)
        dep = result.next()
        
        for dependency in list(dep.triples()):

            # create context features and language elements for each dependency
            
            c1 = ("@", dependency[1], dependency[2])
            c2 = (dependency[0], dependency[1], "@")
            w1 = dependency[0]
            w2 = dependency[2]

            # update all corresponding dictionaries
            dict_update(dependency, bims)
            dict_update(c1, context)
            dict_update(c2, context)
            dict_update(w1, elements)
            dict_update(w2, elements)

        # store the parser output, most of the time was spent on parsing
        f = open("/Users/ramkishoresaravanan/Desktop/output.txt","a")
        f.write("sentence[" + str(count) + "] = " + str(list(dep.triples())))
        f.write("\n")
        f.close()
        count += 1
        sys.stderr.write(str(count))
        
    return context, elements, bims

# takes in list of parsed sentences as input
# applies holing op and returns appropriate vars
def holingOp(parserOutput):
    context = {}
    elements = {}
    bims = {}
    
    for dependencies in parserOutput:
        for dependency in dependencies:
    
            # for le, cf pairs
            c1 = ("@", dependency[1], dependency[2])
            c2 = (dependency[0], dependency[1], "@")
            w1 = dependency[0]
            w2 = dependency[2]

            # update all corresponding dictionaries
            dict_update(dependency, bims)
            dict_update(c1, context)
            dict_update(c2, context)
            dict_update(w1, elements)
            dict_update(w2, elements)
                                    
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
