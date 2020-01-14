import donnees
import modele
import sql


def test_modele():
    q1 = sql.recupererQuestion('FQ0428')
    q2 = sql.recupererQuestion('FQ0651')
    print(modele.get_pertinance(q1,q2))

    q1 = sql.recupererQuestion('FQ0251')
    q2 = sql.recupererQuestion('FQ0252')
    print(modele.get_pertinance(q1,q2))
    print()
    print()
    print()
    l = modele.get_liste_pertinance(q1)
    for i in l:
        print(i[0])
        print(i[1])


test_modele()
