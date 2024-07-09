import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
with open("info.txt","r") as f:
    content=f.readline()
    print(content)
    tokens=word_tokenize(content)
    print(tokens)

