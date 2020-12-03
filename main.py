# This program computes a game of war.
# Written by: Thu Aung
# Written on: Sept 17, 2020
# This is my first program in OOP design.

import random
suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# Create class Card.
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank] # Change rank to integer value for comparison.

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Create class Deck.
class Deck:
    def __init__(self):
        # Create an empty list to hold all cards.
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    # Shuffle cards.
    def shuffle(self):
        random.shuffle(self.all_cards)

    # For splitting shuffled cards to two players.
    def deal_one(self):
        return self.all_cards.pop()

# Create class Player.
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # Compare the top cards of both players.
    def remove_one(self):
        return self.all_cards.pop(0)

    # For war, winner takes all cards(original + new cards). Else, add one cards to deck of winner.
    def add_cards(self, new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

# Create players by giving names.
player_one = Player('One')
player_two = Player('Two')

# Create Deck.
new_deck = Deck()
new_deck.shuffle()

# Splits cards to players.
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# Greetings and explain rules.
print('Welcome to the game of WAR!\n\nThis is a card game with two players.\nEach player receive exactly half of a deck containing 52 cards.\nPlayers compare bottom cards.\nPlayer with higher rank of card gets to take all cards that are comparing.\nIf they drew cards with same rank, they enter "WAR" mode.\nAt war, they bet 4 extra cards and the stake is 5 cards each.\nSame rules, compare bottom cards and higher rank take all cards.\nA player wins if another player loses all cards or has less than 6 cards.\n\nEnjoy the game!!!\n\'\'\' P.S This game could sometimes lead to indefinite round.\n\tIf so, please exit and reopen the program.\'\'\'\n')

# Set up the game.
game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}.') # For keeping track how many rounds the game reaches.

    # Check if any one wins yet.
    if len(player_one.all_cards) == 0:
        print('Player One is out of cards.\nPlayer Two Wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two is out of cards.\nPlayer One Wins!')
        game_on = False
        break

    # For both players, create empty lists for adding cards.
    player_one_cards = []
    # Remove cards at index[0] and add to above lists respectively.
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # Check for war.
    war = True
    while war:
        # Check if player one wins. If yes, add cards to deck of player one cards.
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            war = False

        # Check if player two wins. If yes, add cards to deck of player two cards.
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            war = False

        else:
            print('WAR!!!')
            # Check if player one has enough card to play the game.
            if len(player_one.all_cards) < 6:
                print('Player One Cards: ', len(player_one.all_cards))
                print('Player Two Cards: ', len(player_two.all_cards))
                print('Player One does not have enough cards to declare war.\nPlayer Two Wins!')
                game_on = False
                break

            # Check if player one has enough card to play the game.
            elif len(player_two.all_cards) < 6:
                print('Player Two cards: ', len(player_two.all_cards))
                print('Player One Cards: ', len(player_one.all_cards))
                print('Player Two does not have enough cards to declare war.\nPlayer One Wins!')
                game_on = False
                break

            # At war, players take out and bet 4 extra cards.
            else:
                for y in range(6):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())