from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import csv
from sklearn.feature_extraction.text import CountVectorizer


def filtreMotsClefs(sent):
    lemmatizer = WordNetLemmatizer()
    porter = PorterStemmer()
    words = word_tokenize(sent)
    filtre = []
    with open('../../datas/BOW.csv', 'rt') as f:
         reader = csv.reader(f, delimiter=',')
         for row in reader:
             for field in row:
                 for w in words:
                     w1=w
                     w = porter.stem(w.lower())
                     w1 = lemmatizer.lemmatize(w1.lower())
                     if lemmatizer.lemmatize(field.lower()) == w1.lower():
                        filtre.append(w1)
                     elif porter.stem(field.lower()) == w.lower():
                        filtre.append(w)
                     

    return filtre

def testBOW():
    ch = "Have you implemented country policy  countries a policy to ensure you offer the funds within your defined Target Market?"
    print(filtreMotsClefs(ch))

testBOW()


