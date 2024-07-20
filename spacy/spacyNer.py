import spacy
from spacy.training import Example

nlp = spacy.load("en_core_web_sm")
ner = nlp.get_pipe("ner")


ner.add_label("NEW_ENTITY")


TRAIN_DATA = [
    ("Uber blew through $1 million a week", {"entities": [(0, 4, "ORG")]}),
    ("Google rebrands its business apps", {"entities": [(0, 6, "ORG")]})
]

pipe_exceptions = ["ner"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

with nlp.disable_pipes(*unaffected_pipes):
    optimizer = nlp.resume_training()
    for text, annotations in TRAIN_DATA:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], drop=0.5, sgd=optimizer)


doc = nlp("Uber blew through $1 million a week")
for ent in doc.ents:
    print(ent.text, ent.label_)
