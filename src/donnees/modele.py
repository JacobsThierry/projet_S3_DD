import donnees

def distance_type_DD(dd1, dd2): ##distance entre les types de DD
    distance_identique = 0
    distance_common = 1
    distance_diff = 2

    if(dd1 == "Common" or dd2 == "Common"):
        return distance_common
    elif(dd1 == dd2):
        return distance_identique
    else:
        return distance_diff

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
    
    return base

