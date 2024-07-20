import spacy
from itertools import permutations


nlp = spacy.load('en_core_web_sm')

def score_sentence(sentence):
    doc = nlp(sentence)
    return doc.sentiment

def best_sentence(jumbled_sentence):
    words = jumbled_sentence.split()
    perm = permutations(words)
    best = ""
    best_score = float('-inf')
    
    for p in perm:
        candidate = " ".join(p)
        candidate_score = score_sentence(candidate)
        if candidate_score > best_score:
            best_score = candidate_score
            best = candidate
    
    return best

jumbled_sentence = "jumbled a is this sentence"
correct_sentence = best_sentence(jumbled_sentence)
print("Correct Sentence:", correct_sentence)