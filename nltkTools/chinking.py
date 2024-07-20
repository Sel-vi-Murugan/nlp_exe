import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import RegexpParser

text = "The quick brown fox jumps over the lazy dog while barking loudly and chasing a cat."

tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

grammar = r"""
  NP: {<DT>?<JJ>*<NN.*>}
      }<VB|IN>{
  NP: {<NN.*>+}             
  NP: {<DT>?<JJ>*<NN.*>+<CC><NN.*>} 
  VP: {<MD>?<VB.*><NP|PP|CLAUSE>*}
  PP: {<IN><NP>}
  ADJP: {<JJ.*><CC>?<JJ.*>}
  ADVP: {<RB.*>}
  CLAUSE: {<NP><VP>}
  GERUND: {<VBG><NP|PP>*}
  INF: {<TO><VB>}
  AUXVP: {<MD><VB>}
  CONJP: {<CC><VP>}
  PRT: {<RP>}               
  WHNP: {<WP|WDT><NP>}      
  WHADVP: {<WRB><ADVP>}     
  WHPP: {<IN><WHNP>}        
"""

chunk_parser = RegexpParser(grammar)

tree = chunk_parser.parse(pos_tags)

for subtree in tree:
    if isinstance(subtree, nltk.Tree):
        print(subtree)

tree.draw()
