#libary
import spacy
import pandas as pd
from unidecode import unidecode
from nltk import corpus
import nltk

stop_words = corpus.stopwords.words('portuguese')
nlp = spacy.load('pt_core_news_sm')
nltk.download('stopwords')

def lemma_enumerate(x):
  list_lemma = []
  for n, m in enumerate(x):
    list_lemma.append(' '.join([x.lemma_ for x in nlp(m)]))
  return pd.Series(list_lemma) 

def accent(X):
  return pd.Series([unidecode(x).replace('<UNK>', '') for x in X])