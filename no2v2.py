import os
import re
import nltk
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
import codecs
# nltk.download()
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

#list of strings for each file
data = []

files = os.listdir('txtFiles')
# print(files)
for x in range(len(files)):
	with codecs.open('txtFiles/'+files[x], 'r', encoding='utf8') as myfile:
	    data.append(myfile.read().replace('\n', ''))


pattern = re.compile("\w+")
for x in range(data):
	words.append(re.findall(pattern,data[x]))

for x in range(len(words)):
	words[x] = words[x].lower()
# print(len(words))

file = codecs.open('stop-word-list.txt', 'r', encoding='utf8')
stop_words = file.read().splitlines()

#wrong
for x in range(len(words)):
	for i in range(words[x]):
		words_no_stops[x][i] = [w for w in words[x][i] if not w in stop_words]

# print(len(words))

words_stemmed = []
stemmer = PorterStemmer()
stemmer2 = SnowballStemmer("english")

for i in range(len(words)):
	for x in range(len(words[i])):
		words_stemmed.append(stemmer2.stem(words[i][x]))

print(words_stemmed)
# print(word_tokenize(data))
