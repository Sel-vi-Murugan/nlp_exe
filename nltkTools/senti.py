from nltk.tokenize import sent_tokenize
from textblob import TextBlob
text="okay. moderate. good. very bad. excellent. boring. not nice."
tokens=sent_tokenize(text)
positive_reviews=[]
negative_reviews=[]
for token in tokens:
    blob=TextBlob(token)
    senti=blob.sentiment
    # print(senti)
    pol_Points=senti.polarity
    subjec_points=senti.subjectivity
    if pol_Points>0:
        positive_reviews.append(token)
    else:
        negative_reviews.append(token)
print(len(positive_reviews),"positive reviews =>",positive_reviews)
print(len(negative_reviews),"negative commands =>",negative_reviews)

#def sentenceTokenize(text):
#def sentimentAnalysis(reviews):
# return tokens
# return senti.polarity
# review_cmd=sentenceTokenize(text)
