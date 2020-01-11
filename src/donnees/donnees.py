import xml.etree.ElementTree as ET
import bagOfWord

class question:
    
    def __init__(self, donnee): ##crée une question a partire d'une ligne de donnée
        self.id = get_id(donnee)
        self.typeOfDD = get_type(donnee)
        self.categorie = get_categ(donnee)
        self.shortName = get_sn(donnee)
        self.text = get_texte(donnee)
        self.typeOfAnswer = get_typpe_of_answ(donnee)
        self.keyWords = bagOfWord.filtreMotsClefs(self.text)

    def printData(self):
        print(self.id)
        print("\t", self.typeOfDD)
        print("\t", self.categorie)
        print("\t", self.shortName)
        print("\t", self.text)
        print("\t", self.typeOfAnswer)
        print("\t", self.keyWords)

    def printType(self):
        print(self.id)
        print("\t", type(self.typeOfDD))
        print("\t", type(self.categorie))
        print("\t", type(self.shortName))
        print("\t", type(self.text))
        print("\t", type(self.typeOfAnswer))
        print("\t", type(self.keyWords))

def importData(emplacement):
    tree = ET.parse(emplacement)
    
    return tree.getroot()

def getData():
    donnee = importData("../../datas/Questions_IUT_121219.xml")
    dt = []
    for t in donnee:
        for q in t:
            laq = question(q)
            dt.append(laq)
    return dt

def printdata(donnee):
    for t in donnee:
        for child in t:
            data = question(child)
            data.printData()
    
def get_id(donnee):
    return donnee.tag

def get_type(donnee):
    for typee in donnee.findall("Type_of_DD"):
        return (typee.text)


def get_categ(donnee):
    for categ in donnee.findall("Category"):
        return (categ.text)

def get_sn(donnee):
    for sn in donnee.findall("Short_Name"):
        return sn.text

def get_texte(donnee):
    for sn in donnee.findall("Question_Text"):
        return sn.text

def get_typpe_of_answ(donnee):
    for sn in donnee.findall("Type_Of_Answer"):
        return sn.text

def getligne(donnee, string):
     for ligne in donnee.findall(string):
         return ligne



def testData():
    donnee = importData("../../datas/Questions_IUT_121219.xml")
    #print(question_plus_proche(donnee, donnee[0][0]).tag)
    printdata(donnee)



