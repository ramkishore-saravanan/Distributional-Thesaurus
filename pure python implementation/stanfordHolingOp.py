'''
Corresponds to first five tables in the JoBimText Creation process
1. Sentence
2. Context Feature Extractor
3. Language Element Count
4. Context Feature Count
5. Language Element - Context Feature Count

Author: Ramkishore Saravanan
Computational Linguistics II - Assignment 3:
Distributional thesaurus
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
    '''holing Op on corpus'''
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
    '''holing Op on parsed data'''
    context = {}
    elements = {}
    bims = {}
    
    for dependencies in parserOutput:
        for dependency in dependencies:
    
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
                                    
    return context, elements, bims

if __name__ == "__main__":
    corpus = ["I saw an elephant by the blue river .",
          "We saw the elephant ."]

    context, elements, bims = stanford_le_ce(corpus)
    print context, elements, bims