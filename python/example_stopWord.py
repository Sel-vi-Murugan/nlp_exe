import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
text='This is an example sentence demonstrating stopwords removal.'

words=word_tokenize(text)

stop_word=set(stopwords.words('english'))

remove_stw=[word for word in words if word.lower() not in stop_word]

result=' '.join(remove_stw)
print(result)
