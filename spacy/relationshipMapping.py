import spacy
import networkx as nx
import matplotlib.pyplot as plt


nlp = spacy.load("en_core_web_sm")
sentence = "John likes Mary and they enjoy hiking together."
doc = nlp(sentence)
entities = [(ent.text, ent.label_) for ent in doc.ents]
print("Entities:", entities)
def extract_relationships(doc):
    relationships = []
    for token in doc:
        if token.dep_ in ("attr", "dobj", "pobj", "iobj", "conj"):
            subject = [w.text for w in token.head.lefts if w.dep_ in ("nsubj", "nsubjpass")]
            if subject:
                relationships.append((subject[0], token.text))
        elif token.dep_ in ("nsubj", "nsubjpass"):
            obj = [w.text for w in token.rights if w.dep_ in ("attr", "dobj", "pobj", "iobj")]
            if obj:
                relationships.append((token.text, obj[0]))
        elif token.dep_ == "poss":
            possessor = token.head.text
            possessed = token.text
            relationships.append((possessor, possessed))
    return relationships

relationships = extract_relationships(doc)
print("Relationships:", relationships)

G = nx.Graph()

for ent, label in entities:
    G.add_node(ent, label=label)

for subj, obj in relationships:
    G.add_edge(subj, obj)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", font_color="black", alpha=0.7)
plt.title('Entity Relationships in Sentence')
plt.show()
