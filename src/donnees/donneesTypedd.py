import xml.etree.ElementTree as ET
import bagOfWord
import nltk






class typeofdd:
    def __init__(self, libdd):
        
        self.lib_type_dd = libdd


    def printData(self):
       
        print("\t", self.lib_type_dd)

    def printType(self):
        
        print("\t", type(self.lib_type_dd))

def importData(emplacement):
    tree = ET.parse(emplacement)

    return tree.getroot()


def getDataType():
    donneeType = importData("../../datas/Questions_IUT_121219.xml")
    dt = []
    for t in donneeType:
        for child in t:
            typedd = typeofdd(get_type(child))
            dt.append(typedd)
    return dt





def printdataType(donneeType):
    for t in donneeType:
        for child in t:
            data = typeofdd(get_type(child))
            print(data)


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
    donneeType = importData("../../datas/Questions_IUT_121219.xml")
    #print(question_plus_proche(donnee, donnee[0][0]).tag)

   
    printdataType(donneeType)
