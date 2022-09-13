from pygooglenews import GoogleNews

# default GoogleNews instance

gn = GoogleNews(lang = 'en', country = 'UK')

#Get things by title

def get_titles(search):
    gn = GoogleNews(lang = 'en', country = 'UK')
    search= gn.search(search)
    newsitem= search['entries']
    for item in newsitem:
        print(item.title)
    return

# get_titles("Boris Johnson")

# Get things by link

# def get_titles_links(search):
#     stories = []
#     gn = GoogleNews(lang = 'en', country = 'UK')
#     search= gn.search(search)
#     newsitem= search['entries']
#     for item in newsitem:
#         story = {
#             'title': item.title,
#             'link': item.link
#         }
#         stories.append(story)
#     return print(stories)

# get_titles_links("Queen")


### LONG PASTE OF THE WHOLE ANALYSIS CODE FROM JUPITER NOTEBOOKS


### Imports 

import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re  
import spacy
nlp = spacy.load('en_core_web_lg')

# PLACE THE DATASET BELOW AND PLUG IT INTO ALL SENTENCES 


Title = []

def Top_news():
    gn = GoogleNews(lang = 'en', country = 'UK')
    search= gn.top_news()
    newsitem= search['entries']
    for item in newsitem:
        Title.append(item.title)
    return

# print(top)

Top_news()



# print(Title) 

# Telo = gains_data["body"]


all_sentences = []

for word in Title:
    all_sentences.append(word)
# for word in Telo:
#     all_sentences.append(word)



# all_sentences
#df1 = df.to_string()

#df_split = df1.split()

#df_split
lines = list()
for line in all_sentences:    
    words = line.split()
    for w in words: 
       lines.append(w)



lines = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in lines]

lines

lines2 = []

for word in lines:
    if word != '':
        lines2.append(word)


from nltk.stem.snowball import SnowballStemmer

# The Snowball Stemmer requires that you pass a language parameter
s_stemmer = SnowballStemmer(language='english')

stem = []
for word in lines2:
    stem.append(s_stemmer.stem(word))



stem2 = []

for word in stem:
    if word not in nlp.Defaults.stop_words:
        stem2.append(word)


df = pd.DataFrame(stem2)

df = df[0].value_counts()

from nltk.probability import FreqDist

freqdoctor = FreqDist()

for words in df:
    freqdoctor[words] += 1

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# TOP WORDS PLOT 

df = df[:30,]
sns.set_style('darkgrid')
plt.figure(figsize=(10,5))
sns.barplot(df.values, df.index, alpha=0.8,  palette="Blues_d")
plt.title('Top Words Overall')
plt.ylabel('', fontsize=12)
plt.xlabel('Count of Words', fontsize=12)
plt.show()

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_lg
nlp = en_core_web_lg.load()


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))



str1 = " " 
stem2 = str1.join(lines2)

stem2 = nlp(stem2)

label = [(X.text, X.label_) for X in stem2.ents]

df6 = pd.DataFrame(label, columns = ['Word','Entity'])

df7 = df6.where(df6['Entity'] == 'ORG')

df7 = df7['Word'].value_counts()


# TOP ORGANISATIONS PLOT

df = df7[:20,]
plt.figure(figsize=(10,5))
sns.barplot(df.values, df.index, alpha=0.8,  palette="Blues_d")

plt.title('Top Organizations Mentioned')
plt.ylabel('', fontsize=12)
plt.xlabel('Count of Words', fontsize=12)
plt.show()

str1 = " " 
stem2 = str1.join(lines2)

stem2 = nlp(stem2)

label = [(X.text, X.label_) for X in stem2.ents]

df10 = pd.DataFrame(label, columns = ['Word','Entity'])

df10 = df10.where(df10['Entity'] == 'PERSON')

df11 = df10['Word'].value_counts()

# TOP PEOPLE MENTIONED PLOT

df = df11[:20,]
plt.figure(figsize=(10,5))
sns.barplot(df.values, df.index, alpha=0.8,  palette="Blues_d")
plt.title('Top People Mentioned')
plt.ylabel('', fontsize=12)
plt.xlabel('Count of Words', fontsize=12)
plt.show()





