# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import wordnet

sentence = "I was not happy with the team's performance"
#in here the negation is 'not happy'
#all the models that we have built upto now not consider about this 'not' word
#we need to combine these 'not happy' into one word
#so that we can build a better model

words = nltk.word_tokenize(sentence)

#all words in the new sentence
new_words = []

temp_word = ""

for word in words:
    if word == "not":
        temp_word="not_"
    elif temp_word == "not_":
        word = temp_word+word
        temp_word = ""
    if word != "not":
        new_words.append(word)
      
print(sentence)
print(' '.join(new_words))

#In part 1 what we did was converting 'not happy' to 'not_happy'
new_words=[]
for word in words:
    antonyms = []
    if word == 'not':
        temp_word = 'not_'
    elif temp_word == 'not_':
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_word + word
        temp_word = ''
    if word != 'not':
        new_words.append(word)


print(' '.join(new_words))