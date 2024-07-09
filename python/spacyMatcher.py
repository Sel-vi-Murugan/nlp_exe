import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

pattern = [{"LOWER": "artificial"}, {"LOWER": "intelligence"}]

# Add the pattern to the matcher
matcher.add("AI_PATTERN", [pattern])

# Process some text
text = "Artificial Intelligence (AI) is the field of study that aims to create machines capable of intelligent behavior."
doc = nlp(text)

# Print tokenization and part-of-speech tags for debugging
print("Tokens and POS tags:")
for token in doc:
    print(token.text, token.pos_, token.lower_)

# Apply the matcher to the doc
matches = matcher(doc)

# Print the matches for debugging
print("\nMatches:")
print(matches)

# Print the matched spans
print("\nMatched text:")
for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(f"Matched text: {matched_span.text}")
