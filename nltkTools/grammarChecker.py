import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import RegexpParser


text = "She walk to the market with her friend and buys vegetables."

grammar = r"""
  NP: {<DT>?<JJ>*<NN.*>}
  VP: {<MD>?<VB.*><NP|PP|CLAUSE>*}
  PP: {<IN><NP>}
  CLAUSE: {<NP><VP>}
"""

chunk_parser = RegexpParser(grammar)

def check_grammar(text):
    sentences = sent_tokenize(text)
    errors = []

    for sentence in sentences:
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        tree = chunk_parser.parse(pos_tags)

        for subtree in tree:
            if isinstance(subtree, nltk.Tree):
                if subtree.label() == 'NP':
                    contains_determiner = any(pos == 'DT' for word, pos in subtree.leaves())
                    if not contains_determiner:
                        errors.append(f"Missing determiner in noun phrase: {' '.join(word for word, pos in subtree.leaves())}")

        verb_tenses = set()
        for i in range(len(pos_tags) - 1):
            if pos_tags[i][1].startswith('VB'):
                verb_tenses.add(pos_tags[i][1])
                if pos_tags[i][1] == 'VB' and pos_tags[i+1][1] == 'VBZ':
                    errors.append(f"Incorrect verb form: {' '.join([pos_tags[i][0], pos_tags[i+1][0]])}")

            if pos_tags[i][1] in ['NN', 'NNS', 'NNP', 'NNPS'] and pos_tags[i+1][1] in ['VB', 'VBP', 'VBZ']:
                subject = pos_tags[i][0]
                verb = pos_tags[i+1][0]
                if pos_tags[i][1] == 'NN' and pos_tags[i+1][1] in ['VB', 'VBP']:
                    errors.append(f"Incorrect verb form for singular noun '{subject}': '{verb}'")
                elif pos_tags[i][1] == 'NNS' and pos_tags[i+1][1] == 'VBZ':
                    errors.append(f"Incorrect verb form for plural noun '{subject}': '{verb}'")

        if len(verb_tenses) > 1:
            errors.append(f"Inconsistent verb tenses found in sentence: '{sentence}'")

    return errors

errors = check_grammar(text)
if errors:
    for error in errors:
        print("Grammar error:", error)
else:
    print("No grammar errors found.")

tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
tree = chunk_parser.parse(pos_tags)
tree.draw()
