# -*- coding: utf-8 -*-
import random

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

#N of N-gram model; in here it is Tri-gram
n =6

ngrams = {}

#creating the N-grams
for i in range(len(text)-n):
    gram = text[i:i+n]#ignores the upper limit 
    if gram not in ngrams.keys():
        ngrams[gram]=[]
    ngrams[gram].append(text[i+n])

#Testing N-gram model

currentGram = text[0:n]

result = currentGram

#to generate a text of 100 characters
for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += nextItem
    currentGram = result[len(result)-n:len(result)]

print(result)