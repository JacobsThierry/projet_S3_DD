import donnees
import sql
from operator import itemgetter


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
    distance_diff = 1
    if(c1 == c2):
        return distance_diff
    else:
        return distance_identique
    


def pertinance_base(q1, q2):
    base = 0
    for kw in q1.keyWords:
        if kw in q2.keyWords:
            base+=2
        else:
            base-=2
    for kw in q2.keyWords:
        if kw not in q1.keyWords:
            base-=1
    
    base -= distance_type_DD(q1.typeOfDD, q2.typeOfDD)
    base -= distance_categ_DD(q1.categorie, q2.categorie)

    return base

def get_pertinance(q1,q2):
    
    per = pertinance_base(q1,q2)

    for kw in q1.keyWords:
        if kw in q2.keyWords:
            per += sql.get_pertinance_kw(q2)
    per+= sql.get_pertinance_type_dd(q2, q1.typeOfDD)
    per+=sql.get_pertinance_categorie(q2, q1.categorie, reduction_type_dd)
    per+=sql.get_pertinance_global(q2)
    
    
    return 

def get_liste_pertinance(q1): #retourne une liste de tuple (question, pertinance) dans l'ordre de la plus pertinance a la moins pertinante
    questions = sql.recupererQuestions()
    liste = []
    for q2 in questions:
        if(q1.id != q2.id):
            liste.append((q2, get_pertinance(q1,q2)))
    l2 = sorted(liste, key=itemgetter(1), reverse=True)
    return l2


def update_pertinance_rejete(ques_source, question_proposer):
    reduction_kw = -1
    reduction_type_dd = -1
    reduction_categorie = -1
    reduction_global = -1
    for kw in ques_source.keyWords:
        if kw in question_proposer.keyWords:
            sql.update_pertinance_kw(ques_proposer, kw, reduction_kw)
    sql.update_pertinance_type_dd(ques_proposer, ques_source.typeOfDD, reduction_type_dd)
    sql.update_pertinance_categorie(ques_proposer, ques_source.categorie, reduction_type_dd)
    sql.update_pertinance_global(ques_proposer, reduction_global)


def update_pertinance_choisi(ques_source, question_proposer):
    reduction_kw = 5
    reduction_type_dd = 5
    reduction_categorie = 5
    reduction_global = 5
    for kw in ques_source.keyWords:
        if kw in question_proposer.keyWords:
            sql.update_pertinance_kw(ques_proposer, kw, reduction_kw)
    sql.update_pertinance_type_dd(ques_proposer, ques_source.typeOfDD, reduction_type_dd)
    sql.update_pertinance_categorie(ques_proposer, ques_source.categorie, reduction_type_dd)
    sql.update_pertinance_global(ques_proposer, reduction_global)


def update_pertinance_waiting_list(question_proposer):
    reduction_global = 5
    sql.update_pertinance_global(ques_proposer, reduction_global)








