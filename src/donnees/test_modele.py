import modele
import sql


def test():
    q1 = sql.recupererQuestion("FQ0404")
    q2 = sql.recupererQuestion("FQ0361")
    modele.update_pertinance_rejete(q1, q2)
    q2 = sql.recupererQuestion("FQ0135")
    modele.update_pertinance_choisi(q1, q2)
    print(modele.calculer_pourcentage(q1,q2))


    q1 = sql.recupererQuestion("FQ0361")
    q2 = sql.recupererQuestion("FQ0312")
    print(q1.shortName)
    print(q1.text)
    lp = modele.get_liste_pertinance(q1)
    for i in range(5):
        print(lp[i][0])
        print(modele.calculer_pourcentage(lp[i][0], q1))
    
test()
