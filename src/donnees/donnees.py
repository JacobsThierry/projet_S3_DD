import xml.etree.ElementTree as ET
import bagOfWord
import nltk


class question:
    def __init__(self, idd,typee,categ,sn,t,toa, kw = None, pertinanc = 0): ##crée une question a partire d'une ligne de donnée
        self.id = idd
        self.typeOfDD = typee
        self.categorie = categ
        self.shortName = sn
        self.text = t
        self.typeOfAnswer = toa
        self.pertinance = pertinanc
        if(kw == None):
            self.keyWords = bagOfWord.filtreMotsClefs(self.text)
        else:
            self.keyWords = kw

    def __str__(self):
        kwl = ""
        for i in self.keyWords:
            kwl += i + "; "
        return ("id = " + self.id + " type = " + self.typeOfDD + " categorie = " + self.categorie + " short name = " + self.shortName +
                " text = " + self.text + " type of answer = " + self.typeOfAnswer + " key words : " + kwl + "pertinance : " + str(self.pertinance) +"\n"
                )

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
        for child in t:
            laq = question(get_id(child), get_type(child), get_categ(child), get_sn(child), get_text(child), get_typpe_of_answ(child))
            dt.append(laq)
    return dt

def printdata(donnee):
    for t in donnee:
        for child in t:
            data = question(get_id(child), get_type(child), get_categ(child), get_sn(child), get_text(child), get_typpe_of_answ(child))
            print(data)

def get_id(donnee):
    return donnee.tag

def findQ(Q):
    donnee = importData("../../datas/Questions_IUT_121219.xml")
    for t in donnee:
        for child in t:
            if get_text(child)==Q:

                laq=question(get_id(child), get_type(child), get_categ(child), get_sn(child), get_text(child), get_typpe_of_answ(child))
                return laq

def get_type(donnee):
    for typee in donnee.findall("Type_of_DD"):
        return (typee.text)


def get_categ(donnee):
    for categ in donnee.findall("Category"):
        return (categ.text)

def get_sn(donnee):
    for sn in donnee.findall("Short_Name"):
        return sn.text

def get_text(donnee):
  for sn in donnee.findall("Question_Text"):
        return sn.text

def get_typpe_of_answ(donnee):
    for sn in donnee.findall("Type_Of_Answer"):
        return sn.text

def getligne(donnee, string):
     for ligne in donnee.findall(string):
         return ligne

def get_pertinance(donnee):
    for pertinanc in donnee.findall("Pertinence"):
        return pertinanc

def testData():
    donnee = importData("../../datas/Questions_IUT_121219.xml")
    #print(question_plus_proche(donnee, donnee[0][0]).tag)
    printdata(donnee)
