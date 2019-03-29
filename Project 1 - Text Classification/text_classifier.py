# -*- coding: utf-8 -*-
import numpy as np
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
nltk.download('stopwords')


#importing dataset
#this dataset contains 1000 positive and 1000 negative moview reviews that are classified by humans
reviews = load_files('reviews/')
x,y = reviews.data,reviews.target
#x contains the different reviews
#y contains the different classes 0 or 1 (0 negative since neg is the first folder 1 positive)

#persisting the dataset
#avoiding loading reviews from files everytime because it takes a long time
#so we need to store them as Pickle file of byte type files
#w for write b for byte
with open('x.pickle','wb') as f:
    pickle.dump(x,f)
    
with open('y.pickle','wb') as f:
    pickle.dump(y,f)


#to unpickle a pickled file
with open('x.pickle','rb') as f:
    x = pickle.load(f)
    
with open('y.pickle','rb') as f:
    y = pickle.load(f)
    
#The above method reduces the time of loading data from a great amount than loading them from a file
    

#pre-processing the data

#Creating the corpus (corpus- a list of documents)
corpus = []

for i in range(0,len(x)):
    review = re.sub(r'\W',' ',str(x[i])) #removes all the non word characters, punctuations, ASCIIS
    review = review.lower() #convert the list to lowercase
    review = re.sub(r'\s+[a-z]\s+',' ',review) #removing all single characteres
    review = re.sub(r'^[a-z]\s+',' ',review) #removing single characters at the start of the sentence
    review = re.sub(r'\s+',' ',review) #remove all multiple spaces 
    corpus.append(review)
    

#Creating the model that we are going to feed to the machine learning algorithm

#In here we are not going to directly create the TF-IDF model, instead we create the bow model and
#then create TF-IDF by using that model

from sklearn.feature_extraction.text import CountVectorizer
#CountVectorizer class creates the BOW model for us at this time

#max_features -  how many most frequent words that we are taken to account
#min_df - when you select most frequent words from histogram; then this will exclude all the words that appears in 3 or less than 3 documents
#max_df - exclude all the most frequent words that appears in more than 60% of documents
#Then this method gives us the most frequent 2000 words from the rest after exclusions
vectorizer = CountVectorizer(max_features=2000,min_df=3,max_df=0.6,stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()

#Creating TF-IDF model from BOW model
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
X = transformer.fit_transform(X).toarray()




#Directly create the TF-IDF vectorizer because when we save this model we want to save this vecto also.
#With the above approach we need to save the both transformer and vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
#TfidfVectorizer class creates the TF-IDF model for us at this time
vectorizer = TfidfVectorizer(max_features=2000,min_df=3,max_df=0.6,stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()
#fit_transform(corpus) build the vectorizer based on the corpus




#Creating training and test set

#Split our dataset into training set and testing set
from sklearn.model_selection import train_test_split

#20% of data will be used to test 
#sent_train different sentiment classes associated with text_train
#sent_test different sentiment classes associated with text_test
text_train,text_test,sent_train,sent_test=train_test_split(X,y,test_size=0.2,random_state=0)

#Training our dataset using text_train and sent_train

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()

#To train
classifier.fit(text_train,sent_train)


#Testing Model Performance

#Will predict the text_test
sent_pred = classifier.predict(text_test)

#sent_test is the human classified result
#sent_pred is the machine classified result

#To find out how accurate our model is

from sklearn.metrics import confusion_matrix

cm= confusion_matrix(sent_test,sent_pred)

#columns represent actual values
#rows represent calculated values

#168+171=339 correct results
#339/400=84.75 accuracy of our model


#Saving our Model

with open('classifier.pickle','wb') as f:
    pickle.dump(classifier,f)
    
#Pickling the vectorizer
with open('tfidfmodel.pickle','wb') as f:
    pickle.dump(vectorizer,f)


#Importing and using our model
    
with open('classifier.pickle','rb') as f:
    clf= pickle.load(f)
    
with open('tfidfmodel.pickle','rb') as f:
    tfidf= pickle.load(f)

sample = ['You are very gooood']
#In here we do transform instead of fit_transform 
sample = tfidf.transform(sample).toarray()

print(clf.predict(sample))

