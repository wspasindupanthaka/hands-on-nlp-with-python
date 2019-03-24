# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import nltk

# Sample Data
dataset = ["The amount of polution is increasing day by day",
           "The concert was just great",
           "I love to see Gordon Ramsay cook",
           "Google is introducing a new technology",
           "AI Robots are examples of great technology present today",
           "All of us were singing in the concert",
           "We have launch campaigns to stop pollution and global warming"]

dataset = [line.lower() for line in dataset]

#To build the TF-IDF vector this time, we use built in class

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

print(X[0])

#Decompose X into SVD
#n_components = number of concepts
#n_iter = number of iterations
lsa = TruncatedSVD(n_components=4,n_iter=100)
lsa.fit(X)


row1 = lsa.components_[0]
#this is Vnxr^T that has r rows and n columns
# r is number of concepts
# n is the number of words
# lsa.components_[0] returns the first row of Vnxr^T; first concept
# words in this concept have high value, and others have low value
"""
        | word1 | word 2 | word 3 | word 4 |
concept1|
concept2|
concept3|
concept4|
"""

terms = vectorizer.get_feature_names()

concept_words = {}

for i,comp in enumerate(lsa.components_):
    #combine 2 lists and create a tuple list
    componentTerms = zip(terms,comp)
    sortedTerms  = sorted(componentTerms,key = lambda x:x[1],reverse=True)
    #key = lambda x:x[1] sorts the list based on the comp value of componentTerms
    sortedTerms = sortedTerms[:10]
    print("inConcept",i,":")
    for term in sortedTerms:
        print(term)
    concept_words["Concept "+str(i)] = sortedTerms   
    
        
#Part 2 - Deciding under which concept these word groups are categorized

for key in concept_words.keys():
    sentence_scores=[]
    for sentence in dataset:
        words = nltk.word_tokenize(sentence)
        score=0
        for word in words:
            for word_with_score in concept_words[key]:
                #if word is in word list of concept; then the score of that word is added
                if word == word_with_score[0]:
                    score += word_with_score[1]
        sentence_scores.append(score)
    print("\n"+key+":")
    for sentence_score in sentence_scores:
        print(sentence_score)
        
#Music, Food, Technology, Pollution
"""
Concept 0:
1.1297395470753921
1.4959427190164005
0
0.18383834567413454
0.7797604325216749
1.3733655989909488
0

when considering about the above output the sentence that matches to the Concept 0 most is 
sentence 2.
We know that Concept 0 is about Music. Sentence 2 is also about Music.

By doing this we can know what is Concept 0, Concept 1 etc
After knowing that we can input another set of sentences and know their concepts
"""
pollution = """Air pollution has always accompanied civilizations.
 Pollution started from prehistoric times, when man created the first fires.
 According to a 1983 article in the journal Science, "soot" found on ceilings of prehistoric caves provides ample evidence of the high levels of pollution that was associated with inadequate ventilation of open fires."[4] Metal forging appears to be a key turning point in the creation of significant air pollution levels outside the home. Core samples of glaciers in Greenland indicate increases in pollution associated with Greek, Roman, and Chinese metal production."""

pollution_sentences = nltk.sent_tokenize(pollution)

print("-----------------------------")

for key in concept_words.keys():
    sentence_scores=[]
    for sentence in pollution_sentences:
        words = nltk.word_tokenize(sentence)
        score=0
        for word in words:
            for word_with_score in concept_words[key]:
                #if word is in word list of concept; then the score of that word is added
                if word == word_with_score[0]:
                    score += word_with_score[1]
        sentence_scores.append(score)
    print("\n"+key+":")
    for sentence_score in sentence_scores:
        print(sentence_score)    