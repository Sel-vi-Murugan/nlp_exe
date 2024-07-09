import tkinter as tk
import spacy
import language_tool_python

nlp = spacy.load('en_core_web_sm')

tool = language_tool_python.LanguageTool('en-US')

# Function to tokenize and POS tag the text
def tokenize_and_tag(text):
    doc = nlp(text)
    tokens_pos = [(token.text, token.pos_) for token in doc]
    return tokens_pos

# Function to check grammar using language_tool_python
def check_grammar(text):
    matches = tool.check(text)
    return matches

# Function to suggest corrections for the grammatical errors
def suggest_corrections(matches, text):
    corrections = []
    for match in matches:
        corrections.append({
            'error': match.context,
            'message': match.message,
            'suggestions': match.replacements,
            'offset': match.offset,
            'length': match.errorLength
        })

    corrected_text = list(text)
    offset_diff = 0

    for correction in corrections:
        start = correction['offset'] + offset_diff
        end = start + correction['length']
        if correction['suggestions']:
            suggestion = correction['suggestions'][0]
            corrected_text[start:end] = suggestion
            offset_diff += len(suggestion) - correction['length']

    return corrections, ''.join(corrected_text)

# Main function to combine tokenization, tagging, and grammar checking
def grammar_checker_corrector(text):
    # Tokenize and POS tagging
    tokens_pos = tokenize_and_tag(text)
    
    # Check grammar
    matches = check_grammar(text)
    corrections, corrected_text = suggest_corrections(matches, text)
    
    return tokens_pos, corrections, corrected_text

# Example usage
text = input("enter text...")
tokens_pos, corrections, corrected_text = grammar_checker_corrector(text)

print("Tokens and POS Tags:")
for token, pos in tokens_pos:
    print(f"{token}: {pos}")

print("\nCorrections:")
for correction in corrections:
    print(f"Error: {correction['error']}")
    print(f"Message: {correction['message']}")
    print(f"Suggestions: {', '.join(correction['suggestions'])}\n")

print("Corrected Text:")
print(corrected_text)




# import spacy
# import language_tool_python

# nlp = spacy.load('en_core_web_sm')

# tool = language_tool_python.LanguageTool('en-US')

# def tokenize_and_tag(text):
#     doc = nlp(text)
#     return [(token.text, token.pos_) for token in doc]

# def check_grammar(text):
#     matches = tool.check(text)
#     return matches

# def suggest_corrections(matches):
#     corrections = []
#     for match in matches:
#         corrections.append({
#             'error': match.context,
#             'message': match.message,
#             'suggestions': match.replacements
#         })
#     return corrections

# def grammar_checker_corrector(text):

#     tokens_pos = tokenize_and_tag(text)

#     matches = check_grammar(text)
#     corrections = suggest_corrections(matches)
    
#     return corrections

# text = "I am would be the most stronger in the worldwide."
# corrections = grammar_checker_corrector(text)

# for correction in corrections:
#     print(f"Error: {correction['error']}")
#     print(f"Message: {correction['message']}")
#     print(f"Suggestions: {', '.join(correction['suggestions'])}")
