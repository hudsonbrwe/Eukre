import random
import os
import time
import myUtilities
import gamePlay
import pickingTrumpFuncs
from magic import playingcards as p


#Initializes each teams score
userScore = 0
enemyScore = 0

#YOU ARE PLAYER 1, THE PERSON NEXT TO YOU IS PLAYER 2, THE PERSON ACROSS FROM YOU IS PLAYER 3, THE PERSON TO YOUR LEFT IS PLAYER 4

myUtilities.hold ("Euchre is a four-player card game where you and your partner team up to win at least three out of the five rounds each hand. Winning all five rounds results in 2 points for you and your partner, the first team to 5 points wins the game. At the beginning you will collectively pick a suit to be trump, the highest trump in a round wins that round. You must follow the suit of the first person to lay a card each round, and the Jacks of the trumps colour are the most powerful cards in the game. Enjoy! (Enter to Continue)")

#Loops game until a team wins
while userScore < 5 and enemyScore < 5:

  #make a deck of cards
  myDeck = p.Deck()

  #Makes a Euchre deck
  for j in range (4):
    for i in range(7):
      myDeck.remove_card(1 + (6 * j))
    
  myDeck.shuffle()
  
  #Initiates the game, finding each players hand     
  dealer, myHand, playerTwoHand, partnerHand, playerFourHand, upCard = pickingTrumpFuncs.initiate_game(myDeck)
  
  #Shows your cards and readies the user to decide trump
  gamePlay.show_cards(myHand, upCard, False, False, False)
  hold = input("Decide if you want the up card to be trump, enter 'see cards' at any point in the trump picking process to see your cards   (Enter to Continue)")
  os.system('clear')

  #Runs the function to pick trump
  trump = pickingTrumpFuncs.pick_trump (dealer, myHand, upCard, playerTwoHand, playerFourHand)

  #Runs the main game
  score, winner = gamePlay.main_game(myHand, playerTwoHand, partnerHand, playerFourHand, trump, myDeck)

  #Adds the score to the teams indevidual score
  if winner == "user":
    userScore += score
  else:
    enemyScore += score

  myUtilities.hold (f"Score: \n\nYou + Partner: {userScore} \n\nYour Opponents: {enemyScore}")
