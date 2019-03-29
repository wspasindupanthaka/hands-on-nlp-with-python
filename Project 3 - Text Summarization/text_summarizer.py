# -*- coding: utf-8 -*-
#pip install beautifulsoup4
#pip install lxml

import bs4 as bs
import urllib.request
import re
import nltk
nltk.download('stopwords')
import heapq

#Getting this from Wikipedia

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

soup = bs.BeautifulSoup(source,'lxml') #lxml is a parser to parse an html document

#getting the string out of this parsed document

text = ""

for paragraph in soup.find_all('p'): #fetch all text within <p> tag
    text += paragraph.text
    

#Preprocessing the text
text = re.sub(r"\[[0-9]*\]"," ",text)
text = re.sub(r"\s+"," ",text)


#in here we don't use the text; since important numbers also may get lost from summary
#this purpose of this clean text is to build to histogram only
clean_text = text.lower()
clean_text = re.sub(r'\W',' ',clean_text)
clean_text = re.sub(r'\d',' ',clean_text)
clean_text = re.sub(r'\s+',' ',clean_text)

#we dont care the stopwords when building the histogram
stop_words = nltk.corpus.stopwords.words('english')

word2count = {}

for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word]=1
        else:
            word2count[word]+=1
            

for key in word2count.keys():
    word2count[key] = word2count[key]/max(word2count.values())



#calculating sentence scores
sentences = nltk.sent_tokenize(text)

sent2score = {}
for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word2count.keys():
            if len(sentence.split(' ')) < 30: #To overcome the effect of longer sentences getting more score problem
                if sentence not in sent2score.keys():
                    sent2score[sentence] = word2count[word]
                else:
                    sent2score[sentence] += word2count[word]
                    
                    
#getting the summary
best_sentences = heapq.nlargest(25,sent2score,key=sent2score.get)

print('----------------------------------------------------------------')

print(' '.join(best_sentences))
