import spacy
import neuralcoref
from spacy import displacy
from textblob import TextBlob

nlp=spacy.load('en_core_web_sm')

neuralcoref.add_to_pipe(nlp)

text=nlp(input("Enter a Text: "))

print("Word In The Text: ")
for i in text:
    words=i.text
    print(words)

print("StopWords In The Text: ")
for i in text:
    if not i.is_stop:
        swords=i.text
        print(swords)

print("Lemma In The Text: ")
print("Token : Lemma")
for i in text:
    lemma=i.lemma_
    print(f"{i.text}  :  {lemma}")

print("POS In The Text: ")
for i in text:
    pos=i.pos_
    tag=spacy.explain(i.tag_)
    print(f"{i.text} : {pos} : {tag}")

print("NER In The Text: ")
for i in text.ents:
    print(f"{i.text} : {i.label_}")

print("Sentiment In The Text: ")
blob=TextBlob(text.text)
sentiment=blob.sentiment
print(f"Sentiment : {sentiment}")


print("Corefrence ResolutionIn The Text: ")
if text._.has_coref:
    rtext=text._.coref_resolved
    for cluster in text._.coref_clusters:
        print(cluster.mentions)
    print("Resolved text:", rtext)



displacy.serve(text,style="ent")