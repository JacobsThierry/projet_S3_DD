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
    sql.ajouterDonneesCategDansBDD()
    sql.ajouterDonneesTypeddDansBDD() 


def test_recupererQuestions():
    print(sql.recupererQuestions())

def test_recupererCategories():
	print(sql.test_recupererCategories())

def test_recupererTypeofdds():
	print(sql.test_recupererTypeofdds())

testBDD()
#test_kw()
print(test_recupererQuestions())
print(test_recupererCategories())
print(test_recupererTypeofdds())
