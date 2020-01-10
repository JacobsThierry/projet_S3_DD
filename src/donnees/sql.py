import donnees
import sqlite3


def getConnection():
    conn = sqlite3.connect('../../datas/bdd.sql')
    return conn



def creeBDD():
    conn = getConnection()
    c = conn.cursor()
    c.execute(''' CREATE TABLE QUESTION
    (id text PRIMARY KEY, typeOfDD text, categorie text, shortName text, text text, typeOfAnswer text )''')
    c.execute(''' CREATE TABLE KEYWORD
                    (id INTEGER PRIMARY KEY, word text)''')
    keyw = []

    with open('../../datas/BOW.csv') as fp:
        line = fp.readline()
        keyw.append(line.strip())

    
    c.execute(''' CREATE TABLE POSSEDE
                    (id_q text, id_kw integer)''')
    for w in keyw:
        
        c.execute(''' INSERT INTO KEYWORD(word) VALUEs (?) ''', (w,))

def ajouterDonneeDansBDD(donnee, c):
    data = [donnee.id, donnee.typeOfDD, donnee.categorie, donnee.shortName,
            donnee.text, donnee.typeOfAnswer]
    c.execute('INSERT INTO QUESTION VALUES (?,?,?,?,?,?)', data)
    
    


def ajouterDonneesDansBDD():
    dt = donnees.getData()
    conn = getConnection()
    c = conn.cursor()
    for i in dt:
        ajouterDonneeDansBDD(i,c)
    conn.commit()

def recupererQuestion():
    conn = getConnection()
    c = conn.cursor()
    dt = []
    for row in c.execute('SELECT * FROM QUESTION'):
        print(row)


def creeAjouter():
    creeBDD()
    ajouterDonneesDansBDD()

creeBDD()
