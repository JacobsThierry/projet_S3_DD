import donnees
import sqlite3


def getConnection():
    conn = sqlite3.connect('../../datas/bdd.db')
    return conn



def creeBDD():
    conn = getConnection()
    c = conn.cursor()
    c.execute(''' CREATE TABLE QUESTION
    (id text PRIMARY KEY, typeOfDD text, categorie text, shortName text, text text, typeOfAnswer text, pertinance INTEGER DEFAULT 0 )''')
    
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
        if row[0] != None:
            return row[0]
    c.execute(''' INSERT INTO KEYWORD (word) VALUEs (?) ''', (kw,))
    conn.commit()
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
    try:
        id_q = question.id
    except:
        id_q = question
    conn = getConnection()
    c = conn.cursor()
    kwl = []
    for row in c.execute(''' SELECT word FROM POSSEDE, KEYWORD WHERE id_q = (?) AND id_kw = KEYWORD.id''', (id_q,)):
        kwl.append(row[0])
    return kwl

def ajouterDonneeDansBDD(donnee, c):
    data = [donnee.id, donnee.typeOfDD, donnee.categorie, donnee.shortName,
            donnee.text, donnee.typeOfAnswer, donnee.pertinance]
    c.execute('INSERT INTO QUESTION VALUES (?,?,?,?,?,?, ?)', data)
    for kw in donnee.keyWords:
        id_kw = get_kw_id(kw)
        c.execute(''' SELECT * FROM POSSEDE WHERE id_q = ? AND id_kw = ? ''', (data[0], id_kw))
        r = c.fetchone()
        if r == None:
            c.execute('INSERT INTO POSSEDE VALUES (?,?)', (data[0], id_kw))
        
        
    

def updateDonneeDansBDD(donnee, c):
    data = [donnee.id, donnee.typeOfDD, donnee.categorie, donnee.shortName,
           donnee.text, donnee.typeOfAnswer, donnee.pertinance]
    c.execute('UPDATE QUESTION SET (?,?,?,?,?,?,?)', data)
    print(donnee.keyWords)
    for kw in donnee.keyWords:
        id_kw=get_kw_id(kw)
        c.execute('''UPDATE POSSEDE SET id_q=? AND id_kw = ?''',[data[0],id_kw])

def deleteDonneeDansBDD(donnee, c):
    data = [donnee.id, donnee.typeOfDD, donnee.categorie, donnee.shortName,
           donnee.text, donnee.typeOfAnswer]
    c.execute('DELETE FROM QUESTION WHERE id_q = ?',(data[0]))
    print(donnee.keyWords)
    for kw in donnee.keyWords:
        id_kw=get_kw_id(kw)
        c.execute('''DELETE POSSEDE WHERE id_q=? AND id_kw = ?''',[data[0],id_kw])



def ajouterDonneesDansBDD():
    dt = donnees.getData()
    conn = getConnection()
    c = conn.cursor()
    for i in dt:
        ajouterDonneeDansBDD(i,c)
    conn.commit()

def recupererQuestions():
    conn = getConnection()
    c = conn.cursor()
    dt = []
    for row in c.execute('SELECT * FROM QUESTION'):
        q = donnees.question(row[0],row[1], row[2], row[3], row[4], row[5])
        q.keyWords = get_kw_q(q.id)
        q.pertinance = row[6]
        if q != None:
            dt.append(q)
    return dt

def recupererQuestion(q_id):
    conn = getConnection()
    c = conn.cursor()
    for row in c.execute('SELECT * FROM QUESTION WHERE QUESTION.id = (?)', (q_id,)):
        q = donnees.question(row[0],row[1], row[2], row[3], row[4], row[5])
        qkw = get_kw_q(q.id)
        q.keyWords = get_kw_q(q.id)
        q.pertinance = row[6]
    return q


def creeAjouter():
    creeBDD()
    ajouterDonneesDansBDD()
