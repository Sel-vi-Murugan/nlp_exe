import nltk
from googletrans import Translator
from nltk.tokenize import sent_tokenize
# nltk.download("punkt")

def translation_process(text,srcLang='en',desLang='fr'):
    translator=Translator()
    sentences=sent_tokenize(text)
    translated_sentences=[]
    for sentence in sentences:
        translation=translator.translate(sentence,src=srcLang,dest=desLang)
        translated_sentences.append(translation.text)
    translated_text=' '.join(translated_sentences)
    return translated_text

inp=input("enter text: ")
print(translation_process(inp,srcLang='en',desLang='fr'))