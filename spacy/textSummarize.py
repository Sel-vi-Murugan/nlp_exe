import spacy
import pytextrank

nlp = spacy.load("en_core_web_lg")

nlp.add_pipe("pytextrank")

original_text = '''Indian Institute of Technology Madras (popularly known as IITM or IIT Madras) is a public technical 
university located in Chennai, Tamil Nadu, India. It is one of the eight public Institutes of Eminence of India. The Indian Institutes of Technology (IITs) are autonomous public technical and research universities located across India. 
They are governed by the Institutes of Technology Act, 1961, which has declared them as institutions of national importance and lays down their powers, duties, and framework for governance. 
The Institutes of Technology Act, 1961 lists twenty-three institutes. Each IIT is autonomous, linked to the others through a common council (IIT Council), which oversees their administration. 
The Minister of Education is the ex officio Chairperson of the IIT Council. As of 2021, the total number of seats for undergraduate programs in all IITs is 16,234.'''

doc = nlp(original_text)

summary = doc._.textrank.summary(limit_phrases=2, limit_sentences=2)
for sent in summary:
    print(sent)
