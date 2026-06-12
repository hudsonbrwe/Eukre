import random
import os
import time
import gamePlay




def wait (message):  #Dispayes a message with a wait   #Copied from other code
  waitTime = 0.1
  os.system('clear')
  for i in range (3):
    print (message)
    time.sleep(waitTime)
    os.system('clear')
    print (message+".")
    time.sleep(waitTime)
    os.system('clear')
    print (message+"..")
    time.sleep(waitTime)
    os.system('clear')
    print (message+"...")
    time.sleep(waitTime)
    os.system('clear')


def str_validator(question, validAnswers, myHand, upCard, trumpPicked, makingDecision, trump): #Validates a string input to make sure the user is inputing a valid input, also shows the players cards when "show cards" is inputed
  while True:
    var = str.lower(input(question))
    if var == "show cards":
      gamePlay.show_cards(myHand, upCard, trumpPicked, makingDecision, trump)
    else:
      for i in range (len(validAnswers)):
        if var == validAnswers[i]:
          return var
      print ("ERROR")




def input_validator_int (onlyPositive, message): #Validates int inputs to 
  while True:
    try:
      userInput = int(input(message))
      if onlyPositive == True and userInput >= 0:
        return (userInput)
      elif onlyPositive == True and userInput < 0:
        print ("ERROR")
      elif onlyPositive == False:
        return (userInput)
    except:
      print ("ERROR")




def hold(message):
  holder = input (message)
  os.system('clear')


def set_card_val (card):
    if card.value != 1:
      return card.value
    else:
      return 14
