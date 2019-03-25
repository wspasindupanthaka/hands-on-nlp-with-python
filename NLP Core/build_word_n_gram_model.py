# -*- coding: utf-8 -*-
import random
import nltk

text = """Galle (Sinhalese: ගාල්ල; Tamil: காலி) is a major city in Sri Lanka, situated on the southwestern tip, 119 km from Colombo. Galle is the administrative capital of Southern Province, Sri Lanka and is the district capital of Galle District.

Galle was known as Gimhathiththa[1](although Ibn Batuta in the 14th century refers to it as Qali[2]) before the arrival of the Portuguese in the 16th century, when it was the main port on the island. Galle reached the height of its development in the 18th century, during the Dutch colonial period. Galle is the best example of a fortified city built by the Portuguese in South and Southeast Asia, showing the interaction between Portuguese architectural styles and native traditions. The city was extensively fortified by the Dutch during the 17th century from 1649 onwards. The Galle fort is a world heritage site and is the largest remaining fortress in Asia built by European occupiers.

Other prominent landmarks in Galle include the city's natural harbour, the National Maritime Museum, St. Mary's Cathedral founded by Jesuit priests, one of the main Shiva temples on the island, and Amangalla, the historic luxury hotel. On 26 December 2004, the city was devastated by the massive tsunami caused by the 2004 Indian Ocean earthquake, which occurred off the coast of Indonesia a thousand miles away. Thousands were killed in the city alone. Galle is home to the Galle International Stadium, which is considered to be one of the most picturesque cricket grounds in the world.[3] The ground, which was severely damaged by the tsunami, was rebuilt and test matches resumed there on 18 December 2007.

Important natural geographical features in Galle include Rumassala in Unawatuna, a large mound-like hill that forms the eastern protective barrier to Galle Harbour. Local tradition associates this hill with some events of Ramayana, one of the great Hindu epics. The major river in the area is the Gin River (Gin Ganga), which begins from Gongala Kanda, passes villages such as Neluwa, Nagoda, Baddegama, Thelikada and Wakwella, and reaches the sea at Ginthota. The river is bridged at Wakwella by the Wakwella Bridge."""

n=3

ngrams={}

words = nltk.word_tokenize(text)

for i in range(len(words)-n):
    gram = " ".join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram]=[]
    ngrams[gram].append(words[i+n])
    
currentGram = " ".join(words[0:n])

result = currentGram

for i in range(30):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += " "+nextItem
    rwords = nltk.word_tokenize(result)
    currentGram = " ".join(rwords[len(rwords)-n:len(rwords)])

print(result)