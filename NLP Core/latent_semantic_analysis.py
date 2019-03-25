# -*- coding: utf-8 -*-
"""
A technique that specify overall concept of document

For each of concept we need a set of keywords

Music - Doc1, Doc2
Food - Doc5, Doc3
News - Doc9, Doc5
Tech - Doc1, Doc4

Some articles can have multiple concepts. We can define the probabilities of concepts of those
articles
Doc1 85% Music and 15% Tech

First build the Bag of Words Model

SVD - Singular Value Decomposition

Amxn = Umxr * Srxr * Vnxr^T

Usages
______

Article Bucketing in Websites
Finding relations between articles/words
Page indexing in search engines (Finding documents where most amount of related keywords to search
query is included)



"""
