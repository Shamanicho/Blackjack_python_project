from prettytable import PrettyTable
from Games.Games_instructions.Games_instruction import Blackjack
import random #Library for random picking cards
import os #Library for enter line breaks
import time #Library for delays



program_on=True
reset_game=True
start_game=True

cards_val = {
   "A":11,
   "J":10,
   "Q":10,
   "K":10,
}

cards = [2,3,4,5,6,7,8,9,10,"A","J","Q","K"]
deck = 4 * cards

start_cards = 0

player_cards_picked = []
player_cards_picked_val = []
player_ace_check=False

dealer_cards_picked = []
dealer_cards_picked_val =[]
dealer_2nd_card=0
dealer_ace_check=False

results_table = PrettyTable([], header=False)

error_message = "I do not understand. Please write correct command."

print('''Welcome to Blackjack! 

Please type:

help -> for instruction how game works
start -> to start the game
quit -> if you want to close the game
''')

while program_on:
   player_command = input(":")

   if player_command.upper()=="HELP":
      Blackjack().bj_instruction()
   elif player_command.upper()=="QUIT":
      print("Thanks for play!")
      time.sleep(1)
      exit()

   elif player_command.upper()=="START":

      while start_game:
         reset_game=True
         print("Dealing card...")
         time.sleep(3)  # To make game more real with time delay between picking cards
         #Player 1st 2 cards
         for i in range(0,2):
            first_card = random.choice(deck)
            deck.remove(first_card)
            player_cards_picked.append(first_card)
            player_cards_picked_val.append(cards_val.get(first_card, first_card))

         #Dealer 1st 2 cards
         for i in range(0, 2):
            first_card = random.choice(deck)
            deck.remove(first_card)

            #Hiding 2nd card
            if i==0:
               dealer_cards_picked.append(first_card)
               dealer_cards_picked_val.append(cards_val.get(first_card, first_card))
            else:
               dealer_2nd_card=first_card
               dealer_cards_picked.append("??")


         results_table.add_row(["Player cards", "", "Dealer cards"])
         results_table.add_row([player_cards_picked, "", dealer_cards_picked], divider=True)
         results_table.add_row(["Player cards value", "", "Dealer cards value"])
         results_table.add_row([sum(player_cards_picked_val), "", sum(dealer_cards_picked_val)])
         print(results_table)
         print(f'Dealer 2nd card test: {dealer_2nd_card}')                                                                #To delete later. Just for testing "hidden" card

         while reset_game:

            game_on = True  # This is (I think) needed to reset the game
            print(os.linesep+'''Do you want to "Hit" or "Stay" ?''')
            player_command = input(":")

            if player_command.upper() == "HIT":
               print("Dealing card...")
               time.sleep(3)  # To make game more real with time delay between picking cards

               next_card = random.choice(deck)
               deck.remove(next_card)
               results_table.del_row(3)
               player_cards_picked.append(next_card)

               #Check for Ace's value in player cards, if sum of cards is higher than 21 (then Ace should have value "1" instead of "11")
               if "A" in player_cards_picked and player_ace_check==False and sum(player_cards_picked_val)+11>21:
                  player_cards_picked_val.append(-10)
                  player_ace_check=True

               player_cards_picked_val.append(cards_val.get(next_card, next_card))
               results_table.add_row([sum(player_cards_picked_val), "", sum(dealer_cards_picked_val)])
               print(results_table)

               if sum(player_cards_picked_val) > 21:
                  while game_on:
                     print(
                        '''Your value is higher than 21. You lost! ''' + os.linesep*2 + '''Do you wanna try again?(Type "Yes" or "No") ''')
                     player_command = input(":")
                     if player_command.upper() == "YES":
                        player_cards_picked.clear()
                        player_cards_picked_val.clear()
                        dealer_cards_picked_val.clear()
                        dealer_cards_picked.clear()
                        results_table.clear()
                        print("Clearing table...")
                        time.sleep(4)
                        game_on = False
                        reset_game=False
                     elif player_command.upper() == "NO":
                        print("Thanks for play!")
                        time.sleep(1)
                        exit()
                     else:
                        print(error_message)

            elif player_command.upper() == "STAY":


               # The code for dealer picking cards
               time.sleep(1)
               print("Dealer's turn")
               time.sleep(2)
               print("Revealing Dealer's second card")
               time.sleep(3)
               results_table.del_row(3)
               dealer_cards_picked.remove("??")                                                                         # Clearing "hidden" value
               dealer_cards_picked.append(dealer_2nd_card)
               dealer_cards_picked_val.append(cards_val.get(dealer_2nd_card, dealer_2nd_card))
               results_table.add_row([sum(player_cards_picked_val), "", sum(dealer_cards_picked_val)])
               print(results_table)

               while reset_game:

                  if sum(dealer_cards_picked_val) < 17:
                     # Next card
                     first_card = random.choice(deck)
                     deck.remove(first_card)
                     results_table.del_row(3)
                     dealer_cards_picked.append(first_card)

                     # HERE TO DO THINGS NEXT TIME -> STILLL NOT WORKING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                     if "A" in dealer_cards_picked and dealer_ace_check == False and sum(dealer_cards_picked_val) + 11 > 21:
                        dealer_cards_picked_val.append(-10)
                        dealer_ace_check = True

                     dealer_cards_picked_val.append(cards_val.get(first_card, first_card))
                     results_table.add_row([sum(player_cards_picked_val), "", sum(dealer_cards_picked_val)])
                     time.sleep(1)
                     print("Dealing card...")
                     time.sleep(3)
                     print(results_table)
                     print(f'Dealer 2nd card test{dealer_2nd_card}')                                                       #Test to see 2nd dealer card (to delete later)

                     while sum(dealer_cards_picked_val) < 17:
                        # Next cards
                        next_card = random.choice(deck)
                        results_table.del_row(3)
                        dealer_cards_picked.append(next_card)
                        dealer_cards_picked_val.append(cards_val.get(next_card, next_card))
                        results_table.add_row([sum(player_cards_picked_val), "", sum(dealer_cards_picked_val)])
                        time.sleep(1)
                        print("Dealing card...")
                        time.sleep(3)  # To make game more real with time delay between picking cards
                        print(results_table)
                  else:
                     time.sleep(1)
                     print("Comparing...")
                     time.sleep(3)

                     if (sum(dealer_cards_picked_val)>sum(player_cards_picked_val)) and sum(dealer_cards_picked_val)<=21:
                        results_table.add_row(["", "You have lost :c", ""])
                        print(results_table)
                     elif sum(player_cards_picked_val)>sum(dealer_cards_picked_val) or sum(dealer_cards_picked_val)>21:
                        results_table.add_row(["", "You have won :D", ""])
                        print(results_table)
                     elif sum(player_cards_picked_val)==sum(dealer_cards_picked_val) :
                        results_table.add_row(["", "We have a draw :o", ""])
                        print(results_table)

                     print(os.linesep * 2 + "Do you wanna start again?")
                     reset_command=input(":")
                     if reset_command.upper()== "YES":
                        print("Clearing table...")
                        time.sleep(4)
                        player_cards_picked.clear()
                        player_cards_picked_val.clear()
                        dealer_cards_picked_val.clear()
                        dealer_cards_picked.clear()
                        results_table.clear()
                        game_on=False
                        reset_game = False
                        player_ace_check=False
                        dealer_ace_check = False
                     elif reset_command.upper()== "NO":
                        print("Thanks for play!")
                        time.sleep(1)
                        exit()
            else:
               print(error_message)
   else:
      print(error_message)