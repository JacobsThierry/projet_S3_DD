import sql
import os

def test_kw():
    print(sql.get_kw_id("BOW"))

def testBDD(): ##Détruit et recrée la base de donnée local
    path = '../../datas/bdd.db'
    try:
        os.remove(path)
    except:
        pass
    sql.creeBDD()
    sql.ajouterDonneesDansBDD() 

testBDD()
#test_kw()
