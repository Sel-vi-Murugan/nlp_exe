import spacy
nlp=spacy.load("en_core_web_sm")
text=nlp("Miss.July is one of a college girl. She is topper 5 too")
for sentence in text.sents:
    print(sentence)
    for words in sentence:
        # if words.like_num:
            print(words)


# import re
# text="nsjms5 mjkv 125"
# pat=r'[a-zA-Z]'
# alpha=re.findall(pat,text)
# print(alpha)