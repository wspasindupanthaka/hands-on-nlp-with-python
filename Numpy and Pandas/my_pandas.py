# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#Series
x=pd.Series([1,2,3,4,5])

#to add 100 to every element in series
x+100

(x ** 2)+100

#how many numbers are greater than 2 in series
x>2

#any and all
larger_than_2 = x>2

#if any value in larger_than_2 is true; then this is true
larger_than_2.any()

#if all values in larger_than_2 is true; then this is true
larger_than_2.all()

#apply

def f(x):
    if x%2==0:
        return x**2
    else:
        return x**3

#this doen't change the value of x, if we want to change it -> x=x.apply(f)  
x.apply(f)


#converting types
x.astype(np.float64)

#copy
y=x

#changing value of copied object
y[0]=100

#but the above line has changed the 0 element of both y and x too. not what we expected

#to properly copy a series

y = x.copy()
y[0]=100



#Dataframe
#like a list of series bunched together
#series have only one dimension, whereas dataframes can have multi dimensions

data = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(data,columns=["x"])
df


#to get a column as series
dataSeries = df["x"]

#adding more columns to df
df["x_plus_2"] = df["x"]+2

df["x_square"] = df["x"] ** 2

df["x_factorial"] = df["x"].apply(np.math.factorial)

df["is_even"]=df["x"] %2

df = df.drop("is_even",1)

#selecting multiple columns
df[["x","x_plus_2"]]


#Describe
df.describe()


#reading datasets
#main application of pandas
dataset = pd.read_csv("matches.csv")