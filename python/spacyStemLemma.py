import spacy
nlp=spacy.load("en_core_web_sm")
text=nlp("ability eating running walking swimming observation")
for token in text:
    print(token,"|",token.lemma_,"(",token.lemma,")")


# import nltk
# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize
# stemmer=PorterStemmer()
# text="ability eating running walking swimming observation"
# words=word_tokenize(text)
# for token in words:
#     print(token, "|",stemmer.stem(token),"|",token.lemma_)