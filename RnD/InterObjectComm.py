from collections import deque
import random
import string 
import os
import argparse
import sys

class Kingdom:
    kingdomName = ""
    kingdomKing = ""
    kingdomEmblem = ""
    ally = []
    ruler = None
    kingdomInstances = []

    def addToAlly(self,kingdomName):
        if kingdomName not in self.ally:
            self.ally.append(kingdomName)

    def __init__(self,Name,King,Emblem):
        self.kingdomEmblem = Emblem
        self.kingdomKing = King
        self.kingdomName = Name
        self.ally = []
        self.addToAlly(Name)
        self.__class__.kingdomInstances.append(self)
        
    def IdentifyFriendOrFoe(self,kingdomName,message):
        
        if message==self.kingdomEmblem:
            self.addToAlly(kingdomName)
            return True
        else:
            listOfEmblemChrs = [chrs for chrs in self.kingdomEmblem]
            seaserCipher = SesarSalad()
            
            listOfMsgChrs = seaserCipher.seasarSaladDecrypt(self.kingdomEmblem,message)

            for key in listOfEmblemChrs:
                if key in listOfMsgChrs:
                    listOfMsgChrs.pop(listOfMsgChrs.index(key))
                else:
                    return False
            return True 

    def printAllies(self):
        for name in self.ally:
            print(name, end =" ")
    
    @classmethod
    def checkRuler(cls):
        for instance in cls.kingdomInstances:
                if len(instance.ally) >= int(len(cls.kingdomInstances) * 0.75):
                    cls.ruler = instance.kingdomName
        return cls.ruler

    @classmethod
    def isKingdom(cls,strName):
        for instance in cls.kingdomInstances:
            if strName == instance.kingdomName:
                return instance
        return False

    @classmethod
    def cKingdom(cls,strName):
        if cls.isKingdom(strName):
            pass


class Messenger:
    to = ""
    auther = ""
    message = ""

    def __init__(self,auther,to,message):
        self.to = to
        self.auther = auther
        self.message = message

        if isinstance(to,Kingdom) and isinstance(auther,Kingdom):
            if to.IdentifyFriendOrFoe(auther.kingdomName,message):
                auther.addToAlly(to.kingdomName)

class SesarSalad:
    listOfAlphabets = list(map(lambda x:chr(x),range(65,91)))

    def seasarSaladEncrypt(self,kingdomEmblem):
        #Create Template for Cesear cipher 
        #Create a list of Uppercase caracters, then rotate clockwise by no of characters in kingdom's emblem
        encryptedListOfChars = deque(self.listOfAlphabets)
        encryptedListOfChars.rotate(-len(kingdomEmblem))
        
        #Encode characters using Cesear ciper template
        #Encrypt characters of emblem by first getting the index of each char in (0-25), then finding the charcter at same index in list of encrypted charachter 
        encryptedEmblemChars = list(map(lambda x:encryptedListOfChars[ord(x)-65], list(kingdomEmblem)))
        
        #mix the emblem chars with normal ones to obsfucate
        #making sure to have only emblem characters once, not required but OCD
        nonEmblemChars =[item for item in self.listOfAlphabets if item not in encryptedEmblemChars] 
        result = [item for sublist in zip(nonEmblemChars,encryptedEmblemChars) for item in sublist]
        
        return result
        #return encryptedEmblemChars
        

    def seasarSaladDecrypt(self,kingdomEmblem,text):
        #Create a list of Uppercase caracters, then rotate them by no of characters in kingdom's emblem
        dencryptedListOfChars = deque(self.listOfAlphabets)
        dencryptedListOfChars.rotate(-len(kingdomEmblem))
                
        #Find The index of encrypted text and then get corresponding decrypted char at the same index
        decryptedListOfChrs = list(map(lambda x:self.listOfAlphabets[dencryptedListOfChars.index(x)], list(text)))
        
        result = decryptedListOfChrs
        
        return result

def dispatchMessenger(strInputLine):
    toKingdom = Kingdom.isKingdom(strInputLine.split(' ', 1)[0])
    if toKingdom != False:
        Messenger(SPACE,toKingdom,strInputLine.split(' ', 1)[1].replace(" ", "").strip())
        

def tameOfThrones(strFilePath):
    #SPACE.printAllies()
    with open(strFilePath) as input:
        for line in input:
            dispatchMessenger(line)
    if Kingdom.checkRuler() != None:
        Kingdom.isKingdom(Kingdom.checkRuler()).printAllies()
    else:
        print("None")


SPACE = Kingdom("SPACE","Khan","GORILLA") 
LAND = Kingdom("LAND","","PANDA")
WATER = Kingdom("WATER","","OCTOPUS")
ICE = Kingdom("ICE","","MAMMOTH")
AIR = Kingdom("AIR","","OWL")
FIRE = Kingdom("FIRE","","DRAGON")

"""
parser = argparse.ArgumentParser(prog='geektrust.py',
                                usage='%(prog)s path',
                                description='Tame Of Thrones: A Golden Crown.')

parser.add_argument('path',
                    metavar='path',
                    type=str,
                    help='Full path for input text file.')

args = parser.parse_args()
input_path = args.path

if not os.path.isfile(input_path):
    print('The path specified does not exist')
    #sys.exit()
else:
    print("gaya")
    dispatchMessenger(input_path)
"""
tameOfThrones("input1.txt")