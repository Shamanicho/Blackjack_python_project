from prettytable import PrettyTable
from Games import Blackjack
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

cards = [1,2,3,4,5,6,7,8,9,10,"A","J","Q","K"]
deck = 4 * cards

player_cards_picked = []
player_cards_picked_val = []

dealer_cards_picked = []
dealer_cards_picked_val =[]

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
         time.sleep(2)  # To make game more real with time delay between picking cards
         first_card = random.choice(deck)
         deck.remove(first_card)
         player_cards_picked.append(first_card)
         player_cards_picked_val.append(cards_val.get(first_card, first_card))
         print(os.linesep+'''Your cards:''' + os.linesep + f'''{player_cards_picked}''')
         print(os.linesep + f'Value of your cards:{sum(player_cards_picked_val)}')

         while reset_game:

            game_on = True  # This is (I think) needed to reset the game
            print(os.linesep+'''Do you want to "Hit" or "Stay" ?''')
            player_command = input(":")

            if player_command.upper() == "HIT":
               next_card = random.choice(deck)
               deck.remove(next_card)
               player_cards_picked.append(next_card)
               player_cards_picked_val.append(cards_val.get(next_card, next_card))
               print("Dealing card...")
               time.sleep(2)  # To make game more real with time delay between picking cards
               print(os.linesep+'''Your cards:''' + os.linesep + f'''{player_cards_picked}''')
               print(os.linesep + f'Value of your cards:{sum(player_cards_picked_val)}')
               if sum(player_cards_picked_val) > 21:
                  while game_on:
                     print(
                        '''Your value is higher than 21. You lost! ''' + os.linesep*2 + '''Do you wanna try again?(Type "Yes" or "No") ''')
                     player_command = input(":")
                     if player_command.upper() == "YES":
                        player_cards_picked.clear()
                        player_cards_picked_val.clear()
                        print("Clearing table...")
                        time.sleep(2)
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
               if sum(dealer_cards_picked_val) < 17:
                  # First card
                  print("Dealer's turn")
                  time.sleep(1)  # To make game more real with time delay between picking cards
                  first_card = random.choice(deck)
                  deck.remove(first_card)
                  dealer_cards_picked.append(first_card)
                  dealer_cards_picked_val.append(cards_val.get(first_card, first_card))
                  print("Dealing card...")
                  time.sleep(2)
                  print(os.linesep+'''Dealer cards:''' + os.linesep + f'''{dealer_cards_picked}''')
                  print(os.linesep + f'Value of dealer cards: {sum(dealer_cards_picked_val)}')

                  while sum(dealer_cards_picked_val) < 17:
                     # Next cards
                     time.sleep(1)
                     next_card = random.choice(deck)
                     deck.remove(next_card)
                     dealer_cards_picked.append(next_card)
                     dealer_cards_picked_val.append(cards_val.get(next_card, next_card))
                     print("Dealing card...")
                     time.sleep(2)  # To make game more real with time delay between picking cards
                     print(os.linesep+'''Dealer cards:''' + os.linesep + f'''{dealer_cards_picked}''')
                     print(os.linesep + f'Value of Dealer cards: {sum(dealer_cards_picked_val)}')
                  else:
                     time.sleep(1)
                     print("Comparing...")
                     time.sleep(3)
                     #Adding result values to the final table
                     results_table.add_row(["Player cards", "", "Dealer cards"])
                     results_table.add_row([player_cards_picked, "", dealer_cards_picked],divider=True)
                     results_table.add_row(["Player cards value", "", "Dealer cards value"])
                     results_table.add_row([sum(player_cards_picked_val), "", sum(dealer_cards_picked_val)])

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
                        time.sleep(2)
                        player_cards_picked.clear()
                        player_cards_picked_val.clear()
                        dealer_cards_picked_val.clear()
                        dealer_cards_picked.clear()
                        results_table.clear()
                        game_on=False
                        reset_game = False
                     elif reset_command.upper()== "NO":
                        print("Thanks for play!")
                        time.sleep(1)
                        exit()
            else:
               print(error_message)
   else:
      print(error_message)