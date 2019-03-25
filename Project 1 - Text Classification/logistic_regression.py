# -*- coding: utf-8 -*-

#We have to feed the training model to logistic_regression algorithm to bild the classifier

#Logistic regression is mainly used for binary classification like sentiment analysis

#Each sentence is mapped to a point
#if point val > 0.5 it is positive else negative

#Learning algorithm - a specific type of learning algorithm whose performance increases with time.

#Consider the equation

#y = a + bX1 + cX2 + ... + dX2000

#a,b,c,d are coefficients
#X1, X2,... X2000 are independent variables
#y =  dependent variable
#X1, X2 are values of TF-IDF matrix for a sentence
#Logistic Regression finds the optimal values for a,b,c,d
#
#first we can calculate a,b,c,d from given y
#then for an unknown sentence we can calculate y from those a,b,c,d and if y >= 0.5 that is positive else negative

# we want to normalize so that y has to be in -1 - 1 range


#for y>0; y = e(a + bX1 + cX2 + ... + dX2000)

#for y<1; y = e(a + bX1 + cX2 + ... + dX2000)/(e(a + bX1 + cX2 + ... + dX2000)+1)


#check the downloaded lecture for more