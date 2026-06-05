import random
import os
import time
import myUtilities
import pickingTrumpFuncs
from magic import playingcards as p

#make a deck of cards
myDeck = p.Deck()

#Makes a Euchre deck
for j in range (4):
  for i in range(7):
    myDeck.remove_card(1 + (6 * j))
    
myDeck.shuffle()


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


def use_card (myHand, upCard, trumpPicked, message, trump, showCards):
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


def comp_player_turn(leader, compNum, round, hand, trump, leadCard):
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
      
def can_player_use_card (playerHand, playerCard, leadSuit):
  hasLeadSuit = False
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

  
def main_game (myHand, playerTwoHand, partnerHand, playerFourHand, trump):
  winner = round (myHand, playerTwoHand, partnerHand, playerFourHand, trump, 2, 1)
  print (winner)


def findHighCard (cardList):
  for i in range (len(cardList)):
    for j in range (len (cardList)):
      if myUtilities.set_card_val (cardList[i]) > myUtilities.set_card_val (cardList[j]):
        return cardList[i]


def round (myHand, playerTwoHand, partnerHand, playerFourHand, trump, leader, roundNum):
  leadCard = False
  myUtilities.hold ("\n\nStarting Game (Enter to Continue)")
  playerTwoHand, playerTwoCard = compTurn ("The person to your left", leader, 2, roundNum, playerTwoHand, trump, leadCard)
  leadCard = playerTwoCard
  partnerHand, partnerCard = compTurn ("Your partner", leader, 3, roundNum, partnerHand, trump, leadCard)
  playerFourHand, playerFourCard = compTurn ("The person to your right", leader, 4, roundNum, playerFourHand, trump, leadCard)
  os.system ('clear')
  print (f"It is your turn, you must lay a {playerTwoCard.suit_name} because that was what was lead, {trump} is trump, these are the cards laid so far: \n\nThe person to your left: \n{playerTwoCard.img} \n\nYour partner: \n{partnerCard.img} \n\nThe person to your right: \n{playerFourCard.img}\n\n")

  show_cards (myHand, False, True, True, trump)
  while True:
    playerCard = (use_card (myHand, False, True, "What card would you like to lay?", trump, False))
    if can_player_use_card (myHand, playerCard, playerTwoCard.suit_name) == True:
      myHand.remove (playerCard)
      break
    else:
      print (f"ERROR, please lay a {playerTwoCard.suit_name}")
    
  winningCard = findWinner (playerCard, playerTwoCard, partnerCard, playerFourCard, trump, leader, leadCard)
  print (winningCard)
  if winningCard == playerCard:
    return 1
  elif winningCard == playerTwoCard:
    return 2
  elif winningCard == partnerCard:
    return 3
  elif winningCard == playerFourCard:
    return 4

  
def compTurn (position, leader, compNum, round, hand, trump, leadCard):
  myUtilities.wait (f"{position} is thinking")
  card = comp_player_turn (leader, compNum, round, hand, trump, leadCard)
  myUtilities.wait (f"{position} lays a {card}")
  hand.remove(card)
  return hand, card






def findWinner (playerCard, playerTwoCard, partnerCard, playerFourCard, trump, leader, leadCard):
  cardList = [playerCard, playerTwoCard, partnerCard, playerFourCard]
  if playerCard.suit == playerTwoCard.suit == partnerCard.suit == playerFourCard.suit:
    return findHighCard (cardList)
    
  cardsInSuit = []
  trumpCards = []
  for i in range (4):
    if cardList[i].suit == leadCard.suit:
      cardsInSuit.append (cardList[i])
    if cardList[i].suit_name == trump:
      trumpCards.append (cardList[i])
  print (cardsInSuit)
  print (trumpCards)
  if not trumpCards: #Found this method on the google ai summary
    print ("DFSFDF")
    print (findHighCard (cardsInSuit))
    return findHighCard (cardsInSuit)
  else: 
    print (findHighCard (trumpCards))
    return findHighCard (trumpCards)


