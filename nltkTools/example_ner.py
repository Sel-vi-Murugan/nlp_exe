import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

nltk.download('maxent_ne_chunker')
nltk.download('words')

text = "Apple is looking at buying U.K. startup for $1 billion"
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
tree = ne_chunk(pos_tags)

for subtree in tree:
    if hasattr(subtree, 'label'):
        print(' '.join([leaf[0] for leaf in subtree.leaves()]), subtree.label())
