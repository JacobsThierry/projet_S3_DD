import donnees
import modele
import sql


def test_modele():
    q1 = sql.recupererQuestion('FQ0428')
    q2 = sql.recupererQuestion('FQ0651')
    print(modele.pertinance_base(q1,q2))

test_modele()
