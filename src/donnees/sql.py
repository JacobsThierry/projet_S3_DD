import donnees
import sqlite3


def getConnection():
    conn = sqlite3.connect('../../datas/bdd.db')
    return conn



def creeBDD():
    conn = getConnection()
    c = conn.cursor()
    c.execute(''' CREATE TABLE QUESTION
    (id text PRIMARY KEY, typeOfDD text, categorie text, shortName text, text text, typeOfAnswer text )''')
    
    c.execute(''' CREATE TABLE KEYWORD
                    (id INTEGER PRIMARY KEY, word text)''')
    
    c.execute(''' CREATE TABLE POSSEDE
                    (id_q text, id_kw integer)''')
    keyw = []

    with open('../../datas/BOW.csv') as fp:
        line = fp.readline()

        while line:
            keyw.append(line.strip())
            line = fp.readline()
        

    
    
    for w in keyw:
    
        c.execute(''' INSERT INTO KEYWORD (word) VALUEs (?) ''', (w,))
    conn.commit()

def get_kw_id(kw):
    conn = getConnection()
    c = conn.cursor()
    for row in c.execute(''' SELECT id FROM KEYWORD WHERE word = (?) ''', (kw,)):
        return row[0]
    for row in c.execute(''' SELECT id FROM KEYWORD WHERE word = (?) ''', (kw,)):
        return row[0]
    return -1

def get_kw_word(kw_id):
    conn = getConnection()
    c = conn.cursor()
    for row in c.execute(''' SELECT id FROM KEYWORD WHERE word = (?) ''', (kw,)):
        return row[0]
    for row in c.execute(''' SELECT id FROM KEYWORD WHERE word = (?) ''', (kw,)):
        return row[0]
    return -1

def get_kw_q(question):
    id_q = question.id
    conn = getConnection()
    c = conn.cursor()
    
    for row in c.execute(''' SELECT * FROM POSSEDE WHERE id_q = ?''', (id_q,)):
        

def ajouterDonneeDansBDD(donnee, c):
    data = [donnee.id, donnee.typeOfDD, donnee.categorie, donnee.shortName,
            donnee.text, donnee.typeOfAnswer]
    c.execute('INSERT INTO QUESTION VALUES (?,?,?,?,?,?)', data)
    for kw in donnee.keyWords:
        id_kw = get_kw_id(kw)
        c.execute(''' SELECT * FROM POSSEDE WHERE id_q = ? AND id_kw = ? ''', (data[0], id_kw))
        r = c.fetchone()
        if r == None:
            c.execute('INSERT INTO POSSEDE VALUES (?,?)', (data[0], id_kw))
        
        
    
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
        
        dt.append(donnees.question(row[0],row[1], row[2], row[3], row[4]


def creeAjouter():
    creeBDD()
    ajouterDonneesDansBDD()
