# -*- coding: utf-8 -*-
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')

#named entities - 

paragraph = 'The Taj Mahal was built by emperor Shah Jahan who was born Galle who knows Java'

words = nltk.word_tokenize(paragraph)

tagged_words = nltk.pos_tag(words)

named_entity = nltk.ne_chunk(tagged_words)

named_entity.draw()
