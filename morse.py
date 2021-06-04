from grove_library import *
import math
from random import randint
import time

#Dictionary of Morse Code

CIPHER = { 'A':'10', 'B':'0111','C':'0101', 'D':'011', 'E':'1',
           'F':'1101', 'G':'001', 'H':'1111','I':'11', 'J':'1000',
           'K':'010','L':'1011', 'M':'00', 'N':'01','O':'000',
           'P':'1001', 'Q':'0010','R':'101', 'S':'111', 'T':'0',
           'U':'100', 'V':'1110', 'W':'100','X':'0110', 'Y':'0100', 'Z':'0011'}

def takemsg():
    z=input("Enter the message you want to encrypt")
    z=str(z)
    return z

def decrypt1(a,b,c,d):
    x,y= 0,0
    z,j= 0,0
    L=""

    while True:
        x=arduinoDigitalRead(a)   #to input 1/dot
        y=arduinoDigitalRead(b)   #to input 0/dash
        z=arduinoDigitalRead(c)   #to input space
        j=arduinoDigitalRead(d)   #kill switch
        sleep(0.1)
       
        if(x>0):
            L+="1"
            print(L)
            lcdSetBackground(255, 0, 0)
            speakerPlayNote(2,0.1)   #playing a high pitch for 1's
            sleep(0.5)
            speakerPlayNote(0, 2)
       
        elif(y>0):
            L+="0"
            print(L)
            lcdSetBackground(0, 255, 0)
            speakerPlayNote(10,0.1)   #playing a low pitch for 0's
            sleep(0.5)
            speakerPlayNote(0, 2) 
       
        elif(z>0):
            L+=" "
            print(L)
        
        elif(j>0):
        
            break    
    
    return L

#function to encrypt the string from english to Morse

def encrypt(msg):    
    algorithm = '' 
   
    for i in msg: 
        if i != ' ':  
            algorithm += CIPHER[i] + ' '   #using the keys from the dictionar defined globaly 
        else: 
            # 1 space indicates different characters 
            # & 2 space indicates different words 
            algorithm += ' '
  
    return algorithm 
  
# Function to decrypt the string 
# From morse to english 

def decrypt2(msg): 
  
    # Adding extra space in the end so that we can read the last word/letter 
    msg += ' '
  
    decipher = '' 
    citext = ''
    for k in msg: 
   
        if (k != ' '): 
  
            # Counter to keep track of space 
            i = 0
  
            # Storing morse code of a single character 
            citext += k 
  
        # In case of space 
        else: 
            # If i = 1 that indicates a new character 
            i += 1
  
            # If j = 2 that indicates a new word 
            if i == 2 : 
  
                 # Adding space to separate words 
                decipher += ' '
            else: 
  
                # Accessing the keys using their values  
                decipher += list(CIPHER.keys())[list(CIPHER.values()).index(citext)] 
                citext = '' 
  
    return decipher

connection = arduinoInit(0)
lcdInit(connection)
lcdSetBackground(255, 255, 255)
speakerInit(4, connection)
button1Pin = 2
button2Pin = 5
button3Pin = 7
button4Pin = 3
print("Do you want to encrypt(1) or dycrypt(2)")   #To select either to decryp or encrypt

z=int(input())

if z==1:
    message = takemsg()
    result = encrypt(message.upper()) 
    print (result)
    lcdPrintString(result)

else:
    message = decrypt1(button1Pin,button2Pin,button3Pin,button4Pin)
    result=decrypt2(message)
    lcdPrintString(result)
    print (result) 
