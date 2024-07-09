# tokenization
import nltk
from nltk.tokenize import  word_tokenize,sent_tokenize
nltk.download('punkt')

text="ithu attack pandra puli. ithu asara vaikkura puli. ithu athiradi puli"

w_token=word_tokenize(text)
print(w_token)

s_token=sent_tokenize(text)
for tokens in s_token:
    print(tokens)