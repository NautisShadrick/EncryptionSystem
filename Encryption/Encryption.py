import random
import csv


Original = []
Encrypted = []

Decrypted = []
DecryptedText= ''

numList = []
letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def GenList():
        if(len(numList) < 27):
            num = random.randint(1,27)
            if(num not in numList):
                numList.append(num)
                GenList()
            else:
                GenList()
        else:
            print('Encryption Generated \n')
            EncryptionCode = dict(zip(letterList,numList))
            print(EncryptionCode)
            Encrypt(EncryptionCode)

def Encrypt(code):
    global Encrypted
    global Dencrypted
    Encrypted.clear()
    Decrypted.clear()
    Original.clear()
    
    inp = input("\nEncrypt >> ").lower()
    for x in inp:
        Original.append(x)
    for y in Original:
            Encrypted.append(code[y])
    print(Encrypted)
    input("\nExit ")

## Test For Key And Code in SAme Directory
def first():

    try:
        from key import Key
        from letter import letter
        Decrypt(letter,Key)
    except:
        print("No key Generating Encryption...")
        EncryptionCode = {}
        
        GenList()


def Decrypt(message, EncriptionKey):
    global Decrypted
    Decrypted.clear()
    global DecryptedText

    for number in message:
        for let, num in EncriptionKey.items():
            if(num == number):
                Decrypted.append(let)
                
    display = ''
    for string in Decrypted:
        display += string
    DecryptedText = display
    print(DecryptedText)
    input("\n")

first()

#UNI PHONE NUMBER 3192736218


