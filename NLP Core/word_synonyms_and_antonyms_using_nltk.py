# -*- coding: utf-8 -*-

"""We use wordnet in here that contains all the words with their synonyms"""

import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    #syn.lemmas() gives all the words in that synset
    print(syn.lemmas())
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())

#removed all the duplicates
print(set(synonyms))
print(set(antonyms))