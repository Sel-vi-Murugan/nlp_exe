import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer=PorterStemmer()
text="ability eating running walking swimming observation"
words=word_tokenize(text)
for token in words:
    print(token, "|",stemmer.stem(token),"|",token.lemma_)