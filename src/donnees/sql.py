import donnees
import sqlite3

import donneesCateg
import donneesTypedd


def getConnection():
    conn = sqlite3.connect('../../datas/bdd.db', timeout=30)
    return conn



def creeBDD():
    conn = getConnection()
    c = conn.cursor()
    c.execute(''' CREATE TABLE QUESTION
                    (id text PRIMARY KEY, id_type_dd INTEGER, id_categ INTEGER , shortName text, text text, typeOfAnswer text, pertinance INTEGER DEFAULT 0 )''')

    c.execute(''' CREATE TABLE KEYWORD
                    (id INTEGER PRIMARY KEY, word text)''')

    c.execute(''' CREATE TABLE POSSEDE
                    (id_q text, id_kw integer, pertinence integer DEFAULT 0)''')
    
    c.execute(''' CREATE TABLE TYPE_OF_DD
                    (id_type_dd INTEGER PRIMARY KEY, lib_type_dd TEXT)''')
    
    c.execute('''CREATE TABLE CATEGORIE
                    (id_categ INTEGER PRIMARY KEY, lib_categ TEXT)''')
    
    c.execute('''CREATE TABLE PERTINANCE_CATEGORIE
                    (id_q text, id_categ INTEGER, pertinence INTEGER DEFAULT 0)''')
    
    c.execute('''CREATE TABLE PERTINANCE_TYPE
                    (id_q text, id_type_dd INTEGER, pertinence INTEGER DEFAULT 0)''')

    keyw = []
    
    with open('../../datas/BOW.csv') as fp:
        line = fp.readline()

        while line:
            keyw.append(line.strip())
            line = fp.readline()

    for w in keyw:
        c.execute(""" INSERT INTO KEYWORD (word) VALUEs (?) """, (w.lower(),))
    
    conn.commit()
    conn.close()

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
    conn.close()
    return kwl

def ajouterDonneeDansBDD(donnee, c):

    c.execute('SELECT * FROM CATEGORIE WHERE lib_categ = (?)', (donnee.categorie, ))
    r = c.fetchone()
    if r == None:
        c.execute('INSERT INTO CATEGORIE (lib_categ) VALUES (?)', (donnee.categorie,))

    for row in c.execute('SELECT id_categ FROM CATEGORIE WHERE lib_categ = (?)', (donnee.categorie, )):
        id_categ = row[0]
        
    
    c.execute('SELECT * FROM TYPE_OF_DD WHERE lib_type_dd = (?)', (donnee.typeOfDD, ))
    
    r = c.fetchone()
    if r == None:
        c.execute('INSERT INTO TYPE_OF_DD (lib_type_dd) VALUES (?)', (donnee.typeOfDD,))

    for row in c.execute('''SELECT id_type_dd FROM TYPE_OF_DD WHERE lib_type_dd = (?)''', (donnee.typeOfDD,)):
        id_type_dd = row[0]
        
    data = [donnee.id,id_type_dd,id_categ , donnee.shortName,
            donnee.text, donnee.typeOfAnswer, donnee.pertinance]

    c.execute('INSERT INTO QUESTION VALUES (?,?,?,?,?,?,?)', data)

    for kw in donnee.keyWords:
        id_kw = get_kw_id(kw)
        c.execute(''' SELECT * FROM POSSEDE WHERE id_q = ? AND id_kw = ? ''', (data[0], id_kw))
        r = c.fetchone()
        if r == None:
            c.execute('INSERT INTO POSSEDE VALUES (?,?,?)', (data[0], id_kw, 0))

    c.execute('''SELECT * FROM PERTINANCE_CATEGORIE WHERE id_q=? AND id_categ=?''',(data[0],id_categ))
    r2 = c.fetchone()
    if r2 == None:
        c.execute('INSERT INTO PERTINANCE_CATEGORIE VALUES (?,?,?)',(data[0],id_categ,0))

    c.execute('''SELECT * FROM PERTINANCE_TYPE WHERE id_q=? AND id_type_dd=?''',(data[0], id_type_dd))
    r3 = c.fetchone()
    if r3 == None:
        c.execute('INSERT INTO PERTINANCE_TYPE VALUES (?,?,?)',(data[0],id_type_dd,0))

    




def updateDonneeDansBDD(donnee, c):
    data = [donnee.id, donnee.shortName,
           donnee.text, donnee.typeOfAnswer, donnee.pertinance]
    c.execute('UPDATE QUESTION SET (?,?,?,?,?)', data)
    for kw in donnee.keyWords:
        id_kw=get_kw_id(kw)
        c.execute('''UPDATE POSSEDE SET id_q=? AND id_kw = ?''',[data[0],id_kw])

def deleteDonneeDansBDD(donnee, c):
    data = [donnee.id,  donnee.shortName,
           donnee.text, donnee.typeOfAnswer, donnee.pertinance]
    c.execute('DELETE FROM QUESTION WHERE id_q = ?',(data[0]))
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
    conn.close()

def ajouterDonneesCategDansBDD():
    dt = donneesCateg.getDataCateg()
    conn = getConnection()
    c = conn.cursor()
    for i in dt:
        ajouterDonneeDansBDD(i,c)
    conn.commit()

def ajouterDonneesTypeddDansBDD():
    dt = donneesTypedd.getDataType()
    conn = getConnection()
    c = conn.cursor()
    for i in dt:
        ajouterDonneeDansBDD(i,c)
    conn.commit()

def get_lib_text(lib_id):
    conn = getConnection()
    c = conn.cursor()
    for row2 in c.execute('SELECT lib_type_dd FROM TYPE_OF_DD WHERE id_type_dd = (?)', (lib_id,)):
        lib = row2[0]
    conn.close()
    return lib

def get_categ_text(categ_id):
    conn = getConnection()
    c = conn.cursor()
    for row2 in c.execute('SELECT lib_categ FROM CATEGORIE WHERE id_categ = (?)', (categ_id,)):
        categ = row2[0]
    conn.close()
    return categ
        
    

def recupererQuestions():
    conn = getConnection()
    c = conn.cursor()
    dt = []
    for row in c.execute('SELECT * FROM QUESTION'):
        
        type_dd = get_lib_text(row[1])
        categ = get_categ_text(row[2])

        q = donnees.question(row[0], type_dd, categ, row[3], row[4], row[5])
        q.keyWords = get_kw_q(q.id)
        q.pertinance = row[5]
        
        
        if q != None:
            dt.append(q)
    conn.close()
    return dt

def recupererCategories():
    conn = getConnection()
    c = conn.cursor()
    dt = []
    for row in c.execute('SELECT * FROM CATEGORIE'):
        ca = donnees.categorie(row[0], row[1])
        if ca != None:
            dt.append(ca)
    return dt

def recupererTypeofdds():
    conn = getConnection()
    c = conn.cursor()
    dt = []
    for row in c.execute('SELECT * FROM TYPE_OF_DD'):
        td = donnees.typeofdd(row[0], row[1])
        if td != None:
            dt.append(td)
    return dt

def recupererQuestion(q_id):
    conn = getConnection()
    c = conn.cursor()
    for row in c.execute('SELECT * FROM QUESTION WHERE QUESTION.id = (?)', (q_id,)):
        q = donnees.question(row[0],row[1], row[2], row[3], row[4])
        qkw = get_kw_q(q.id)
        q.keyWords = get_kw_q(q.id)
        q.pertinance = row[5]
    return q

def recupererCategorie(categ_id):
    conn = getConnection()
    c = conn.cursor()
    for row in c.execute('SELECT * FROM CATEGORIE WHERE CATEGORIE.id_categ = (?)', (categ_id)):
        ca = donnees.categorie(row[0], row[1])
    return ca    

def recupererTypeofdd(dd_id):
    conn = getConnection()
    c = conn.cursor()
    for row in c.execute('SELECT * FROM TYPE_OF_DD WHERE TYPE_OF_DD.id_type_dd = (?)', (dd_id)):
        td = donnees.typeofdd(row[0], row[1])
    return td


def get_pertinance_type_dd(q2, typeOfDD):
    conn =getConnection()
    c = conn.cursor()
    p = None
    for row in c.execute( ''' SELECT id_type_dd FROM TYPE_OF_DD where lib_type_dd = (?) ''',  (typeOfDD,)):
        tdd = row[0]    
    for row in c.execute( ''' SELECT pertinence from PERTINANCE_TYPE where id_q = (?) and id_type_dd = (?) ''',  (q2.id, tdd)):
        p = row[0]

    if p == None:
        c.execute(''' INSERT INTO PERTINANCE_TYPE VALUES (?, ?, 0) ''', (q2.id, tdd))
        p = 0
        conn.commit()
    
    return p

def get_pertinance_categorie(q2, categorie):
    conn =getConnection()
    c = conn.cursor()
    p = None
    for row in c.execute( ''' SELECT id_categ FROM CATEGORIE where lib_categ = (?) ''',  (categorie,)):
        tdd = row[0]    
    for row in c.execute( ''' SELECT pertinence from PERTINANCE_CATEGORIE where id_q = (?) and id_categ = (?) ''',  (q2.id, tdd)):
        p = row[0]

    if p == None:
        c.execute(''' INSERT INTO PERTINANCE_CATEGORIE VALUES (?, ?, 0) ''', (q2.id, tdd))
        p = 0
        conn.commit()
    return p
    

def get_pertinance_global(q2):
    conn =getConnection()
    c = conn.cursor()
    p = 0
    for row in c.execute(''' SELECT pertinance FROM QUESTION where id = (?) ''', (q2.id,)):
        p = row[0]
    return p

def get_pertinance_kw(q, kw):
    conn =getConnection()
    c = conn.cursor()
    p = None
    kwid =  get_kw_id(kw)
    for row in c.execute(''' SELECT  pertinence FROM POSSEDE where id_q = (?) and id_kw = (?)''', (q.id,kwid)):
        p = row[0]
    if p == None:
        c.execute( ''' INSERT INTO POSSEDE VALUES (?,?,0)''', q.id, kwid)
        conn.commit()
    return p
        

def update_pertinance_type_dd(q, type_dd, modif):
    conn =getConnection()
    c = conn.cursor()
    p = None
    for row in c.execute( ''' SELECT id_type_dd FROM TYPE_OF_DD where lib_type_dd = (?) ''',  (type_dd,)):
        tdd = row[0]    
    for row in c.execute( ''' SELECT pertinence from PERTINANCE_TYPE where id_q = (?) and id_type_dd = (?) ''',  (q.id, tdd)):
        p = row[0]
    if p == None:
        c.execute(''' INSERT INTO PERTINANCE_TYPE VALUES (?, ?, 0) ''', (q2.id, tdd))
        conn.commit()
    
    c.execute(''' UPDATE  PERTINANCE_TYPE SET pertinence = pertinence + (?) WHERE id_q = (?) AND id_type_dd = (?)''', (modif, q.id, tdd))
    conn.commit()

    
    
def update_pertinance_categorie(q2, categorie, modif):
    conn =getConnection()
    c = conn.cursor()
    p = None
    for row in c.execute( ''' SELECT id_categ FROM CATEGORIE where lib_categ = (?) ''',  (categorie,)):
        tdd = row[0]    
    for row in c.execute( ''' SELECT pertinence from PERTINANCE_CATEGORIE where id_q = (?) and id_categ = (?) ''',  (q2.id, tdd)):
        p = row[0]

    if p == None:
        c.execute(''' INSERT INTO PERTINANCE_CATEGORIE VALUES (?, ?, 0) ''', (q2.id, tdd))
        p = 0
        conn.commit()
    c.execute(''' UPDATE  PERTINANCE_CATEGORIE SET pertinence = pertinence + (?) WHERE id_q = (?) AND id_categ = (?)''', (modif, q2.id, tdd))
    conn.commit()

def update_pertinance_kw(q, kw, modif):
    conn =getConnection()
    c = conn.cursor()
    p = None
    kwid =  get_kw_id(kw)
    for row in c.execute(''' SELECT  pertinence FROM POSSEDE where id_q = (?) and id_kw = (?)''', (q.id,kwid)):
        p = row[0]
    if p == None:
        c.execute( ''' INSERT INTO POSSEDE VALUES (?,?,0)''', q.id, kwid)
        conn.commit()
    c.execute(''' UPDATE POSSEDE SET pertinence =  pertinence + (?) WHERE id_q = (?) and id_kw = (?)''', (modif,q.id,kwid))
    conn.commit()
    
def update_pertinance_global(q, modif):
    conn =getConnection()
    c = conn.cursor()
    p = 0
    c.execute(''' UPDATE QUESTION SET pertinance = pertinance + (?) where id = (?) ''', (modif,q.id ))
    conn.commit()



def creeAjouter():
    creeBDD()
    ajouterDonneesDansBDD()
    ajouterDonneesCategDansBDD()
    ajouterDonneesTypeddDansBDD()


