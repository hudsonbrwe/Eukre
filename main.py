import random
import os
import time
import myUtilities
import gamePlay
import pickingTrumpFuncs
from magic import playingcards as p

#make a deck of cards
myDeck = p.Deck()

#Makes a Euchre deck
for j in range (4):
  for i in range(7):
    myDeck.remove_card(1 + (6 * j))
    
myDeck.shuffle()

#YOU ARE PLAYER 1, THE PERSON NEXT TO YOU IS PLAYER 2, THE PERSON ACROSS FROM YOU IS PLAYER 3, THE PERSON TO YOUR LEFT IS PLAYER 4
  

      
      
    
  
    

dealer, myHand, playerTwoHand, partnerHand, playerFourHand, upCard = pickingTrumpFuncs.initiate_game()
gamePlay.show_cards(myHand, upCard, False, False, False)
hold = input("Decide if you want the up card to be trump, enter 'see cards' at any point in the trump picking process to see your cards   (Enter to Continue)")
os.system('clear')
trump = pickingTrumpFuncs.pick_trump (dealer, myHand, upCard, playerTwoHand, playerFourHand)
gamePlay.main_game(myHand, playerTwoHand, partnerHand, playerFourHand, trump)



