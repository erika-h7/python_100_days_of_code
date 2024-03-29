######################## Black Jack Project #################################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

## Imports
import random
from replit import clear

## Logo
logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
'''

## Setting up the constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = "backside"

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns one random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(cards):
    """Take a list of cards and return the score calculates from the cards"""
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    # if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 😙"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack 😱"
    elif user_score == 0:
        return "You win 🏆 with a BlackJack"
    elif user_score > 21:
        return f"You went over with {user_score}, you loose 😔"
    elif computer_score > 21:
        return f"Opponent went over with {computer_score}. You win 🏆"
    elif user_score > computer_score:
        return f"You win with {user_score} 🏆"
    else:
        return "You lose 😔"

def play_game():
    print(logo)
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        """for loop that runs twice without a variable"""
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:
        # Calculates score of user and computer
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
        # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another another card, type 'n' to pass >> ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        # If computer score hasn't won nor lost draw another card
        computer_cards.append(deal_card())
        # Recalculate the computer score
        computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()

    


# def blackjack():
#     play = input("Do you want to play a game of BlackJack? type 'y' or 'n' 👉 ").lower()
#     getdeck()
#
#
# def getdeck():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     your_cards = random.sample(cards, 2)
#
#     # adding the two numbers from your_cards list
#     your_current_score = your_cards[0] + your_cards[1]
#
#     computer_cards = random.sample(cards, 1)
#
#     print(f"Your cards: {your_cards}, Current score: {your_current_score}")
#     print(f"Computer first card: {computer_cards}")
#
#     another_card = input("Type 'y' to get another card, type 'n' to pass 👉 ").lower()
#
#     if your_current_score == 21:
#         print("You win! 🎉")
#     elif your_current_score >= 22:
#         print("You lose! 👎")
#
#     if another_card == "y":
#         new_card = random.sample(cards, 1)
#         your_cards.append(new_card)
#
#         new_score = your_current_score + new_card[0]
#         print(f"Your cards: {your_cards}, Current score: {new_score}")
#
#         if new_score > 21:
#             print("you lose! ")
#
#
# blackjack()
# print(HEARTS)
