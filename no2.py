import os
import re
import nltk
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
import codecs
# nltk.download()
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

files = os.listdir('txtFiles')
# print(files)

with codecs.open('txtFiles/'+files[0], 'r', encoding='utf8') as myfile:
    data=myfile.read().replace('\n', '')


pattern = re.compile("\w+")
words = re.findall(pattern,data)

for x in range(1,10):
	print(words[x])

print(len(words))
for x in range(len(words)):
	words[x]= words[x].lower()

file = codecs.open('stop-word-list.txt', 'r', encoding='utf8')
stop_words = file.read().splitlines()


words = [w for w in words if not w in stop_words]

for x in range(1,10):
	print(words[x])
print(len(words))

words_stemmed = []
stemmer = PorterStemmer()
stemmer2 = SnowballStemmer("english")

for x in range(len(words)):
	words_stemmed.append(stemmer2.stem(words[x]))

for x in range(1,10):
	print(words_stemmed[x])
# print(words_stemmed)
# print(word_tokenize(data))

