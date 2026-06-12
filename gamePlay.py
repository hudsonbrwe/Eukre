import random
import os
import time
import myUtilities
import pickingTrumpFuncs
from magic import playingcards as p




def show_cards(myHand, upCard, trumpPicked, makingDecision, trump): #Shows the user his hand and upCard/Trump   #Copied from old code
  print ("Your Hand:")
  for i in range (len(myHand)):
    if makingDecision == True:
      print (f"{i + 1}:")
    print (myHand[i].img)
  if trumpPicked == False:
    print ("Up Card:")
    print (upCard.img)
  else:
    print (f"\nTrump: {trump}")




def use_card (myHand, upCard, trumpPicked, message, trump, showCards): #Lets the user pick a card to lay/pick as trump
  if showCards == True:
    show_cards (myHand, upCard, trumpPicked, True, trump)
  while True:
    use = myUtilities.input_validator_int (True, message)
    if use > 0 and use <= len(myHand):
      break
    else:
      print ("ERROR")
  removedCard = (myHand[use-1])
  return removedCard




def comp_player_turn(leader, compNum, round, hand, trump, leadCard): #Runs the computers turn for the main gameplay
  valueList = []
  notTrumpValueList = []
  leadCardSuitValueList = []
  hasLeadCardSuit = False
  for i in range (len(hand)):
    valueList.append (myUtilities.set_card_val(hand[i]))
    if hand[i].suit_name != trump:
      if hand[i].value != 1:
        notTrumpValueList.append (hand[i].value)
      else:
        notTrumpValueList.append (14)
    else:
      notTrumpValueList.append (0)
  if leader == compNum:
    return (hand[notTrumpValueList.index(max(notTrumpValueList))])
  else:
    leadCardSuit = leadCard.suit_name
    for i in range (len(hand)):
      if hand[i].suit_name == leadCardSuit:
        leadCardSuitValueList.append (myUtilities.set_card_val(hand[i]))
        hasLeadCardSuit = True
      else:
        leadCardSuitValueList.append (0)
    if hasLeadCardSuit == True:
      return (hand[leadCardSuitValueList.index(max(leadCardSuitValueList))])
    else:
      return (hand[valueList.index(min(valueList))])



      
def can_player_use_card (playerHand, playerCard, leadSuit, trump): #Confirms if a player can use a card, includes exceptions with the left bower
  hasLeadSuit = False
  
  if is_card_left_bower (playerCard, trump) == True:
    if leadSuit == trump:
      return True
    if leadSuit == playerCard.suit_name:
      return False

  
  for i in range (len(playerHand)):
    if (playerHand[i].suit_name) == leadSuit:
      hasLeadSuit = True
  
  if hasLeadSuit == True:
    if playerCard.suit_name == leadSuit: 
      return True
    else:
      return False
  else:
    return True




def is_card_left_bower (card, trump): #Checks to see if a card is the left bower
  if card.value == 11:
    if card.suit == "Hearts" and trump == "Diamonds":
      return True
    elif card.suit == "Diamonds" and trump == "Hearts":
      return True
    elif card.suit == "Spades" and trump == "Clubs":
      return True
    elif card.suit == "Clubs" and trump == "Spades":
      return True
  else:
    return False



  
def main_game (myHand, playerTwoHand, partnerHand, playerFourHand, trump, myDeck): #Runs the main game by using a for i in range function that runs 5 rounds
  winner = 2
  winnerList = []
  userScore = 0
  enemyScore = 0
  myUtilities.hold ("\n\nStarting Game (Enter to Continue)")
  for i in range (5):
    winner = round (myHand, playerTwoHand, partnerHand, playerFourHand, trump, winner, 1)
    winnerList.append (winner)
    os.system ('clear')
    if winner == 1:
      userScore += 1
      myUtilities.hold (f"You Won! \n\nScore:  \n\nYou + Your Partner: {userScore} \n\nYour Oppenents: {enemyScore} (Enter to Continue)")
    elif winner == 3:
      userScore += 1
      myUtilities.hold (f"Your Partner Won! \n\nScore:  \n\nYou + Your Partner: {userScore} \n\nYour Oppenents: {enemyScore} (Enter to Continue)")
    elif winner == 2:
      enemyScore += 1
      myUtilities.hold (f"The person to your left won, \n\nScore:  \n\nYou + Your Partner: {userScore} \n\nYour Oppenents: {enemyScore} (Enter to Continue)")
    elif winner == 4:
      enemyScore += 1
      myUtilities.hold (f"The person to your right won, \n\nScore:  \n\nYou + Your Partner: {userScore} \n\nYour Oppenents: {enemyScore} (Enter to Continue)")
  
  if userScore == 5:
    return 2, "user"
  elif userScore > enemyScore:
    return 1, "user"
  elif enemyScore == 5:
    return 2, "enemy"
  elif enemyScore > userScore:
    return 1, "enemy"

  


def findHighCard (cardList): #Finds the highest card in a list
  if len (cardList) == 1:
    return cardList[0]
  highCard = cardList[0]
  for i in range (len(cardList)):
    if myUtilities.set_card_val (cardList[i]) > myUtilities.set_card_val (highCard):
      highCard = (cardList[i])
  return highCard




def round (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum): #Runs the round based on who is leading including returning the winner
  if leader == 2:
    leadCard, playerCard, playerTwoCard, partnerCard, playerFourCard, myHand, playerTwoHand, partnerHand, playerFourHand = roundForPlayerTwoLeader (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum)
  elif leader == 3:
    leadCard, playerCard, playerTwoCard, partnerCard, playerFourCard, myHand, playerTwoHand, partnerHand, playerFourHand = roundForPartnerLeader (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum)
  elif leader == 4:
    leadCard, playerCard, playerTwoCard, partnerCard, playerFourCard, myHand, playerTwoHand, partnerHand, playerFourHand = roundForPlayerFourLeader (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum)
  elif leader == 1:
    leadCard, playerCard, playerTwoCard, partnerCard, playerFourCard, myHand, playerTwoHand, partnerHand, playerFourHand = roundForUserLeader (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum)

  winningCard = findWinner (playerCard, playerTwoCard, partnerCard, playerFourCard, trump, leader, leadCard)
  if winningCard == playerCard:
    return 1
  elif winningCard == playerTwoCard:
    return 2
  elif winningCard == partnerCard:
    return 3
  elif winningCard == playerFourCard:
    return 4



  
def compTurn (position, leader, compNum, round, hand, trump, leadCard): #Runs the computer players turn including the output and removing the computers laid card
  myUtilities.wait (f"{position} is thinking")
  card = comp_player_turn (leader, compNum, round, hand, trump, leadCard)
  myUtilities.wait (f"{position} lays a {card}")
  hand.remove(card)
  return hand, card




def findWinner (playerCard, playerTwoCard, partnerCard, playerFourCard, trump, leader, leadCard): #Finds the winner of the round based on the led card and trump
  cardList = [playerCard, playerTwoCard, partnerCard, playerFourCard]
  
  for i in range (4):
    if cardList[i].value == 11 and cardList[i].suit_name == trump:
      return cardList[i]

  for i in range (4):
    if is_card_left_bower (cardList[i], trump) == True:
      myUtilities.hold ("Left bower laid")
      return cardList [i]
  
  if playerCard.suit == playerTwoCard.suit == partnerCard.suit == playerFourCard.suit:
    return findHighCard (cardList)
  cardsInSuit = []
  trumpCards = []
  for i in range (4):
    if cardList[i].suit == leadCard.suit:
      cardsInSuit.append (cardList[i])
    if cardList[i].suit_name == trump:
      trumpCards.append (cardList[i])
  if not trumpCards: #Found this method on the google ai summary
    return findHighCard (cardsInSuit)
  else: 
    return findHighCard (trumpCards)



#Rounds based on if each computer is the "leader" could not figure out how to optimize, runs each players turn in a specific order including the users


def roundForPlayerTwoLeader (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum):
  leadCard = False
  playerTwoHand, playerTwoCard = compTurn ("The person to your left", leader, 2, roundNum, playerTwoHand, trump, leadCard)
  leadCard = playerTwoCard
  
  partnerHand, partnerCard = compTurn ("Your partner", leader, 3, roundNum, partnerHand, trump, leadCard)
    
  playerFourHand, playerFourCard = compTurn ("The person to your right", leader, 4, roundNum, playerFourHand, trump, leadCard)
    
  os.system ('clear')
    
  print (f"It is your turn, you must lay a {leadCard.suit_name} because that was what was lead, {trump} is trump, these are the cards laid so far: \n\nThe person to your left: \n{playerTwoCard.img} \n\nYour partner: \n{partnerCard.img} \n\nThe person to your right: \n{playerFourCard.img}\n\n")
  show_cards (myHand, False, True, True, trump)
  while True:
    playerCard = (use_card (myHand, False, True, "What card would you like to lay?", trump, False))
    if can_player_use_card (myHand, playerCard, leadCard.suit_name, trump) == True:
      myHand.remove (playerCard)
      break
    else:
      print (f"ERROR, please lay a {leadCard.suit_name}")

  return leadCard, playerCard, playerTwoCard, partnerCard, playerFourCard, myHand, playerTwoHand, partnerHand, playerFourHand



def roundForPartnerLeader (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum):
  leadCard = False
  partnerHand, partnerCard = compTurn ("Your partner", leader, 3, roundNum, partnerHand, trump, leadCard)
  leadCard = partnerCard

  playerFourHand, playerFourCard = compTurn ("The person to your right", leader, 4, roundNum, playerFourHand, trump, leadCard)
  print (f"It is your turn, you must lay a {leadCard.suit_name} because that was what was lead, {trump} is trump, these are the cards laid so far: \n\nYour partner: \n{partnerCard.img} \n\nThe person to your right: \n{playerFourCard.img}\n\n")
  show_cards (myHand, False, True, True, trump)
  while True:
    playerCard = (use_card (myHand, False, True, "What card would you like to lay?", trump, False))
    if can_player_use_card (myHand, playerCard, leadCard.suit_name, trump) == True:
      myHand.remove (playerCard)
      break
    else:
      print (f"ERROR, please lay a {leadCard.suit_name}")  

  playerTwoHand, playerTwoCard = compTurn ("The person to your left", leader, 2, roundNum, playerTwoHand, trump, leadCard)
  
  return leadCard, playerCard, playerTwoCard, partnerCard, playerFourCard, myHand, playerTwoHand, partnerHand, playerFourHand



def roundForPlayerFourLeader (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum):
  leadCard = False
  playerFourHand, playerFourCard = compTurn ("The person to your right", leader, 4, roundNum, playerFourHand, trump, leadCard)
  leadCard = playerFourCard

  print (f"It is your turn, you must lay a {leadCard.suit_name} because that was what was lead, {trump} is trump, these are the cards laid so far: \n\nThe person to your right: \n{playerFourCard.img}\n\n")
  show_cards (myHand, False, True, True, trump)
  while True:
    playerCard = (use_card (myHand, False, True, "What card would you like to lay?", trump, False))
    if can_player_use_card (myHand, playerCard, leadCard.suit_name, trump) == True:
      myHand.remove (playerCard)
      break
    else:
      print (f"ERROR, please lay a {leadCard.suit_name}")

  playerTwoHand, playerTwoCard = compTurn ("The person to your left", leader, 2, roundNum, playerTwoHand, trump, leadCard)

  partnerHand, partnerCard = compTurn ("Your partner", leader, 3, roundNum, partnerHand, trump, leadCard)

  return leadCard, playerCard, playerTwoCard, partnerCard, playerFourCard, myHand, playerTwoHand, partnerHand, playerFourHand



def roundForUserLeader (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum):
  leadCard = False
  print (f"It is your turn, you are leading, you may lay any card")
  show_cards (myHand, False, True, True, trump)
  
  playerCard = (use_card (myHand, False, True, "What card would you like to lay?", trump, False))
  myHand.remove (playerCard)
  
  leadCard = playerCard

  playerTwoHand, playerTwoCard = compTurn ("The person to your left", leader, 2, roundNum, playerTwoHand, trump, leadCard)

  partnerHand, partnerCard = compTurn ("Your partner", leader, 3, roundNum, partnerHand, trump, leadCard)
    
  playerFourHand, playerFourCard = compTurn ("The person to your right", leader, 4, roundNum, playerFourHand, trump, leadCard)

  return leadCard, playerCard, playerTwoCard, partnerCard, playerFourCard, myHand, playerTwoHand, partnerHand, playerFourHand
