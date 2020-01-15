import donnees
import sql
import bagOfWord
from operator import itemgetter

max_pertinance = 2

def distance_type_DD(dd1, dd2): ##distance entre les types de DD
    distance_identique = 0
    distance_common = 0
    distance_diff = 2

    if(dd1 == "Common" or dd2 == "Common"):
        return distance_common
    elif(dd1 == dd2):
        return distance_identique
    else:
        return distance_diff


def distance_categ_DD(c1, c2): ##distance entre les types de DD
    distance_identique = 0
    distance_diff = 2
    if(c1 == c2):
        return distance_diff
    else:
        return distance_identique
    


def pertinance_base(q1, q2): #vaut au minimum -4 - card(kw) - card(kw_sn) * 2, au maximum 2 * card(kw) + 3 * card(kw_sn)
    base = 0
    for kw in q1.keyWords:
        if kw in q2.keyWords:
            base+=2
        else:
            base-=1
    for kw in q2.keyWords:
        if kw not in q1.keyWords:
            base-=1
    for kw in bagOfWord.filtreMotsClefs(q1.shortName):
        if kw in q2.keyWords:
            base+=3
        elif kw not in q2.text:
            base-=2
    base -= distance_type_DD(q1.typeOfDD, q2.typeOfDD)
    base -= distance_categ_DD(q1.categorie, q2.categorie)

    return base

def get_pertinance(q1,q2):
       
    per = pertinance_base(q1,q2)

    if q2.apparu == 0:
        ratio = 0
    else:
        ratio = q2.choisi/q2.apparu
    print(ratio)
    per+= max_pertinance * ratio
    
    
    
    return per

'''
def get_pertinance_max(q1):#comparer la question saisi avec lui même pour trouver la pertinence MAX

    per = pertinance_base(q1,q1)

    for kw in q1.keyWords:
        if kw in q1.keyWords:
            per += sql.get_pertinance_kw(q1,kw)
    per+=sql.get_pertinance_type_dd(q1,q1.typeOfDD)
    per+=sql.get_pertinance_categorie(q1,q1.categorie)
    per+=sql.get_pertinance_global(q1)

    return per

'''

def get_liste_pertinance(q1): #retourne une liste de tuple (question, pertinance) dans l'ordre de la plus pertinance a la moins pertinante
    questions = sql.recupererQuestions()
    liste = []
    for q2 in questions:
        if(q1.id != q2.id):
            liste.append((q2, get_pertinance(q1,q2)))
    l2 = sorted(liste, key=itemgetter(1), reverse=True)
    print(l2)
    return l2


def update_pertinance_rejete(ques_source, ques_proposer):
    sql.question_rejete(ques_proposer)


def update_pertinance_choisi(ques_source, ques_proposer):
    sql.question_choisi(ques_proposer)


def update_pertinance_waiting_list(ques_proposer):
    reduction_global = 5
    sql.update_pertinance_global(ques_proposer, reduction_global)

def calculer_pourcentage(q_proposer,q_saisi):
    
    v2 = pertinance_base(q_saisi,q_saisi) + max_pertinance
    v1=get_pertinance(q_saisi, q_proposer)

    print()
    print(v1)
    print(v2)
    print()
    
    vp=(v1/v2)*100 

    return vp





