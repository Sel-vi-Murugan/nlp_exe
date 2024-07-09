
# import spacy
# from spacy.pipeline import pytextrank
# nlp=spacy.load("en_core_web_lg")
# nlp.add_pipe("textrank")
# text='''Indian Institute of Technology Madras (popularly known as IITM or IIT Madras) is a public technical 
# university located in Chennai, Tamil Nadu, India. It is one of the eight public Institutes of Eminence of India. 
# As an Indian Institute of Technology (IIT), IIT Madras is also recognised as an Institute of National Importance.
# Founded in 1959 with technical, academic and financial assistance from the then government of West Germany, 
# IITM was the third Indian Institute of Technology established by the Government of India.[6][7] IIT Madras has
# consistently ranked as the best engineering institute in India by the Ministry of Education's National 
# Institutional Ranking Framework since the ranking's inception in 2016.'''
# doc=nlp(text)
# for sent in doc._.textrank.summary(limit_phases=2,limit_sentences=2):
#     print(sent)


# import gensim
# from gensim.summarization import summarize
# original_text='''Indian Institute of Technology Madras (popularly known as IITM or IIT Madras) is a public technical 
# university located in Chennai, Tamil Nadu, India. It is one of the eight public Institutes of Eminence of India. 
# As an Indian Institute of Technology (IIT), IIT Madras is also recognised as an Institute of National Importance.
# Founded in 1959 with technical, academic and financial assistance from the then government of West Germany, 
# IITM was the third Indian Institute of Technology established by the Government of India.[6][7] IIT Madras has
# consistently ranked as the best engineering institute in India by the Ministry of Education's National 
# Institutional Ranking Framework since the ranking's inception in 2016.'''

# short_summary = summarize(original_text)
# print(short_summary)


import spacy
import pytextrank

# Load the spaCy model
nlp = spacy.load("en_core_web_lg")

# Add PyTextRank to the spaCy pipeline
nlp.add_pipe("pytextrank")

# Sample text for summarization
original_text = '''Indian Institute of Technology Madras (popularly known as IITM or IIT Madras) is a public technical 
university located in Chennai, Tamil Nadu, India. It is one of the eight public Institutes of Eminence of India. The Indian Institutes of Technology (IITs) are autonomous public technical and research universities located across India. 
They are governed by the Institutes of Technology Act, 1961, which has declared them as institutions of national importance and lays down their powers, duties, and framework for governance. 
The Institutes of Technology Act, 1961 lists twenty-three institutes. Each IIT is autonomous, linked to the others through a common council (IIT Council), which oversees their administration. 
The Minister of Education is the ex officio Chairperson of the IIT Council. As of 2021, the total number of seats for undergraduate programs in all IITs is 16,234.'''

# Process the text
doc = nlp(original_text)

# Extract and print the summary
summary = doc._.textrank.summary(limit_phrases=2, limit_sentences=2)
for sent in summary:
    print(sent)
