# -*- coding: utf-8 -*-
"""
Markov Chains - States
is a chain of states

->A is a state
->B is a state

prob(A > B) : 50%
prob(A > A) : 50%
prob(B > B) : 50%
prob(B > B) : 50%

All these have same probabilities

AABA - Chain of states, Markov Chain

N-gram is a contiguous sequence of n items from a given sample of text

items refer to states in Markov Chains 

items can be "characters", "words", "sentences"

if N=2 ; bigram > window size is 2
N=3 ; tri-gram > window size is 3

in case of characters, characters are the states of Markov Chain

"the bird is flying on the blue sky"

N=2
Bigrams = 'th','he','e ',' b','bi',.....

N=3
Trigrams = 'the','he ','e b',' bi','bir',....

we will use these data to track the next character following Trigram

used in phone keyboards
used in search term suggestions
used in auto complete article systems
"""
