from transformers import pipeline

nlp = pipeline("question-answering")

context = """
“What is Comprehension” 
The literal meaning of ‘Comprehension’ is understanding. It shows how well you have understood a 
paragraph that you have read or how correctly you have grasped its meaning. To test it, a set of
questions is given after a paragraph relating to the subject matter. The answers are contained 
in the passage. It only requires a bit of intelligence to identify the sentence or sentences 
that form the answer to a particular question.  Write them down in your own hand. It is simple. 
The exercise of comprehension is meant to assess and better the ability of a student to read and 
comprehend what he reads. Sometimes the answers need to be written in the student’s own words, 
although not very different from the given text, only a little adjustment to have the sentence 
grammatically and meaning-wise correct. Hence, a student must be able to express his thoughts 
precisely with incorrect words.
"""
question = input("Ask your questions?")

result = nlp(question=question, context=context)

print(f"Answer: {result['answer']}")
print(f"Score: {result['score']}")
