from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import csv
from sklearn.feature_extraction.text import CountVectorizer


def filtreMotsClefs(sent):
    porter = PorterStemmer()
    words = word_tokenize(sent)
    filtre = []
    with open('../../datas/BOW.csv', 'rt') as f:
         reader = csv.reader(f, delimiter=',')
         for row in reader:
             for field in row:
                 for w in words:
                     w = porter.stem(w.lower())
                     if porter.stem(field.lower()) == w.lower():
                        filtre.append(w)

    return filtre

def testBOW():
    ch = "Have you implemented a policy to ensure you offer the funds within your defined Target Market?"
    print(filtreMotsClefs(ch))

testBOW()
