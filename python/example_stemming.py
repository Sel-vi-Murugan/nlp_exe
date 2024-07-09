from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
# stemmer =PorterStemmer()
string_for_stemming = """
The crew of the USS Discovery discovered many discoveries.
Discovering is what explorers do."""
words=word_tokenize(string_for_stemming)
stemmed_words = [PorterStemmer().stem(word) for word in words]
print(stemmed_words)