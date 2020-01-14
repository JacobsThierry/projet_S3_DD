import xml.etree.ElementTree as ET
import bagOfWord
import nltk




class categorie:
    def __init__(self, lib):
        #self.id_categ = idc
        self.lib_categ = lib


    def printData(self):
        #print(self.id_categ)
        print("\t", self.lib_categ)

    def printType(self):
        #print(self.id_categ)
        print("\t", type(self.lib_categ))



def importData(emplacement):
    tree = ET.parse(emplacement)

    return tree.getroot()



def getDataCateg():
    donneeCateg = importData("../../datas/Questions_IUT_121219.xml")
    dt = []
    for t in donneeCateg:
        for child in t:
            categ = categorie(get_categ(child))
            dt.append(categ)
    return dt




def printdataCateg(donneeCateg):
    for t in donneeCateg:
        for child in t:
            data = categorie(get_categ(child))
            print(data)

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
    donneeCateg = importData("../../datas/Questions_IUT_121219.xml")
    #print(question_plus_proche(donnee, donnee[0][0]).tag)
   
    printdataCateg(donneeCateg)
  
