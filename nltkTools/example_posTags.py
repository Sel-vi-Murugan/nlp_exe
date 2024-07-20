import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download("averaged_perceptron_tagger")
text="Example to execute parts of speech taging in python"
words=word_tokenize(text)
pos_tags=nltk.pos_tag(words)
print(pos_tags)