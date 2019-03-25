# -*- coding: utf-8 -*-
import nltk
import re
import heapq
import numpy as np

paragraph = """Thank you all so very much. Thank you to the Academy. 
Thank you to all of you in this room. I have to congratulate the other incredible 
nominees this year. The Revenant was the product of the tireless efforts of an
unbelievable cast and crew. First off, to my brother in this endeavor, Mr. Tom Hardy.
Tom, your talent on screen can only be surpassed by your friendship off screen … thank 
you for creating a transcendent cinematic experience. Thank you to everybody at Fox and
New Regency … my entire team. I have to thank everyone from the very onset of my career … 
To my parents; none of this would be possible without you. And to my friends, 
I love you dearly; you know who you are.
And lastly, I just want to say this: Making The Revenant was about man's relationship to 
the natural world. A world that we collectively felt in 2015 as the hottest year 
in recorded history. Our production needed to move to the southern tip of this planet 
just to be able to find snow. Climate change is real, it is happening right now. 
It is the most urgent threat facing our entire species, and we need to work collectively
together and stop procrastinating. We need to support leaders around the world who do not
speak for the big polluters, but who speak for all of humanity, for the indigenous people 
of the world, for the billions and billions of underprivileged people out there who would
be most affected by this. For our children’s children, and for those people out there whose
voices have been drowned out by the politics of greed. I thank you all for this amazing
award tonight. Let us not take this planet for granted. I do not take tonight for granted.
Thank you so very much."""


sentences = nltk.sent_tokenize(paragraph)

#cleaning the impurities
for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub(r'\W',' ',sentences[i])
    sentences[i] = re.sub(r'\s+',' ',sentences[i])
#end of part 1

#Creating histogram
word2count = {}

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

#end of part 2

#picking up most frequent 10 words
freq_words = heapq.nlargest(100,word2count,key=word2count.get)

#the above is creating the histogram as in bow model

# IDF Matrix
word_idfs={}

for word in freq_words:
    doc_count=0 #no of documents containing this word
    for sentence in sentences:
        if word in nltk.word_tokenize(sentence):
            doc_count += 1
    word_idfs[word]=np.log((len(sentences)/doc_count)+1) #+1 is kind of bias, is kind of standard
    

#TF Matrix
word_tfs={}

for word in freq_words:
    word_tf=[]
    for sentence in sentences:
        frequency=0
        for w in nltk.word_tokenize(sentence):
            if w==word:
                frequency+=1
        tf_word=frequency/len(nltk.word_tokenize(sentence))
        word_tf.append(tf_word)
    word_tfs[word]=word_tf
    
#TF-IDF calculation
tf_idf_matrix=[]

for word in word_tfs.keys():
    tf_idf=[]
    for value in word_tfs[word]:
        score = value*word_idfs[word]
        tf_idf.append(score)
    tf_idf_matrix.append(tf_idf)
  
#converting to 2d array
x = np.asarray(tf_idf_matrix)

x = np.transpose(x)
