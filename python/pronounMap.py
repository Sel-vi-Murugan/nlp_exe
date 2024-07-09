import spacy
import neuralcoref
text = "John went to the store because he needed milk."
if text._.has_coref:
    rtext=text._.coref_resolved
    for cluster in text._.coref_clusters:
        print(cluster.mentions)
    print("Resolved text:", rtext)

