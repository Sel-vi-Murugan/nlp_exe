import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

pattern = [{"LOWER": "artificial"}, {"LOWER": "intelligence"}]

matcher.add("AI_PATTERN", [pattern])

text = "Artificial Intelligence (AI) is the field of study that aims to create machines capable of intelligent behavior."
doc = nlp(text)

print("Tokens and POS tags:")
for token in doc:
    print(token.text, token.pos_, token.lower_)

matches = matcher(doc)

print("\nMatches:")
print(matches)

print("\nMatched text:")
for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(f"Matched text: {matched_span.text}")
