from collections import deque
import random
import string 

class Kingdom:
    kingdomName = ""
    kingdomKing = ""
    kingdomEmblem = ""
    ally = []
    ruler = ""
    kingdomCount = 0

    def addToAlly(self,kingdomName):
        if kingdomName not in self.ally:
            self.ally.append(kingdomName)

    def __init__(self,Name,King,Emblem):
        self.kingdomEmblem = Emblem
        self.kingdomKing = King
        self.kingdomName = Name
        self.ally = []
        self.kingdomCount+=1
        self.addToAlly(Name)
        
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

    def printAttributes(self):
        print("\n Emblem = ",self.kingdomEmblem,"\n Name of the King =", self.kingdomKing,"\n Name of the Kingdom =",self.kingdomName)
 
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
        #Create a list of Uppercase caracters, then rotate them by no of characters in kingdom's emblem
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
        
        #result = ''.join([str(chr) for chr in decryptedListOfChrs])
        result = decryptedListOfChrs
        
        return result
        



SPACE = Kingdom("SPACE","Khan","GORILLA") 
LAND = Kingdom("LAND","","PANDA")
WATER = Kingdom("WATER","","OCTOPUS")
ICE = Kingdom("ICE","","MAMMOTH")
AIR = Kingdom("AIR","","OWL")
FIRE = Kingdom("FIRE","","DRAGON")

seaserCipher = SesarSalad()


Messenger(SPACE,LAND,"FAIJWJSOOFAMAU")
Messenger(SPACE,WATER,seaserCipher.seasarSaladEncrypt("OCTOPUS"))
Messenger(SPACE,WATER,"OCTOPUS")
Messenger(SPACE,ICE,"STHSTSTVSASOS")
Messenger(SPACE,AIR,"ROZO")
Messenger(SPACE,AIR,seaserCipher.seasarSaladEncrypt("OWL"))
Messenger(SPACE,FIRE,"DRAGON")

for i in SPACE.ally:
    print(i, end =" ")
#def tameOfThrones()
