from cipher import cipher
from saver import saver
from translate import Numcode
from morse import morse
# import all the classes
print('What type of message would you like to send?')
print('Morse Code')
print('Cipher')
print('Numeric')
print('')
messageType=input().lower() #which translation should be used
while messageType!='cipher' and messageType!='morse code' and messageType!='numeric': #go until it works
    print('Sorry, I didn\'t get that, try again?')
    messageType=input().lower()
print('Please type your message here:') #get information about sender, recipient, and message
message=input()
print('For whom is this message?')
location=input()
print('And finally, what\'s your name?')
sender=input()
if messageType=='cipher':
          export=cipher(message)
if messageType=='numeric':
          export=Numcode(message)
if messageType=='morse code':
          export=morse(message)
finish=saver(export.translation, sender, location) #save file using all the given information
