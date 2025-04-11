import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
        'Queen':10, 'King':10, 'Ace':11}

class Card():
    """
    Represents a single playing card with a suit, rank, and corresponding value
    """
    def __init__(self,suit:str,rank:str,value:int):
        self.__suit = suit
        self.__rank = rank
        self.__value = value

    def get_suit(self) ->str:
        return self.__suit
    def get_rank(self) ->str:
        return self.__rank
    def get_value(self) ->str:
        return self.__value
    def __str__(self) -> str:
        return f"{self.__rank} of {self.__suit}"
    
class Deck():
    """
    Represents a full deck of 52 playing cards
    """
    def __init__(self):
        self.__deck_of_cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank,values[rank])
                self.__deck_of_cards.append(card)
    def shuffle(self):
        random.shuffle(self.__deck_of_cards)
    def deal_out(self) -> Card:
        card_dealt = self.__deck_of_cards.pop()
        return card_dealt
    def deck_length(self) -> int:
        return len(self.__deck_of_cards)

class Balance():
    """
    Manages the player's current balance and handles betting transactions
    """
    def __init__(self):
        self.__amount = 100
    def widraw(self,bet:float) ->bool:
        if self.__amount - bet >= 0:
            self.__amount = self.__amount - bet
            return True
        return False
    def add_funds(self,won:float):
        self.__amount += won
    def get_balance(self) ->float:
        return self.__amount

class Hand:
    """
    Represents the hand of a player or dealer, keeping track of cards, total value, and aces
    """
    def __init__(self):
        self.__cards = []  
        self.__value = 0   
        self.__aces = 0 
    
    def add_card(self,card):
        self.__cards.append(card)
        self.__value += values[card.get_rank()]
        if card.get_rank() == 'Ace':
            self.__aces += 1
    
    def adjust_for_ace(self):
        while self.__value > 21 and self.__aces:
            self.__value -= 10
            self.__aces -= 1 
    def get_value(self) ->int:
        return self.__value
    def get_cards(self) ->list:
        return self.__cards
            

class Game():
    """
    Controls the flow of a Blackjack game, including dealing cards, placing bets, and evaluating results
    """
    def __init__(self):
        self.__player_hand = Hand()
        self.__computer_hand = Hand()
        self.__deck = Deck()
        self.__deck.shuffle()
        self.__bet = 0
        self.__balance = Balance()

    def place_bet(self):
        try:
            print(f"Your current amount is {self.__balance.get_balance()}")
            self.__bet = float(input("Please enter your bet: "))
            while(self.__balance.widraw(self.__bet) == False):
                self.__bet = float(input("Your bet cannot be more that your amount. Enter new amount:"))
        except(ValueError):
            print("You have entered invalid data.Try again: ")

    def win(self):
        player_value = self.__player_hand.get_value()
        dealer_value = self.__computer_hand.get_value()

        print(f"\nFinal Hands:")
        print(f"Dealer: {dealer_value}")
        print(f"Player: {player_value}")

        if player_value > 21:
            print("You busted! Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busted! You win!")
            self.__balance.add_funds(2 * self.__bet)
        elif player_value > dealer_value:
            print(f"Congrats! You win {2 * self.__bet}")
            self.__balance.add_funds(2 * self.__bet)
        elif player_value < dealer_value:
            print("You lost.")
        else:
            print("It's a tie! Bet returned.")
            self.__balance.add_funds(self.__bet)

    def print_game_state(self, is_endgame: bool):
        print("Dealer has:")
        if not is_endgame:
            print("_")
            print(self.__computer_hand.get_cards()[1])
        else:
            for y in self.__computer_hand.get_cards():
                print(y)
        print("You have:")
        for y in self.__player_hand.get_cards():
            print(y)

    def reset(self):
        """
        Resets the player and dealer hands and shuffles a new deck if necessary
        """
        self.__player_hand = Hand()
        self.__computer_hand = Hand()
        self.__bet = 0
        if self.__deck.deck_length() < 10:
            self.__deck = Deck()
            self.__deck.shuffle()

    def start_game(self):
        """
        Main game loop. Deals cards, handles player decisions (hit or stand), determines the winner, updates balance, and prompts to continue
        """
        while True:

            self.place_bet()
            deal_outs = 0
            while deal_outs <= 1:
                self.__computer_hand.add_card(self.__deck.deal_out())
                self.__player_hand.add_card(self.__deck.deal_out())
                deal_outs += 1

            is_endgame = False
            self.print_game_state(is_endgame)

            while True:

                choice = input("Do you want to hit or stand? Type h or s: ")
                choice = choice.lower()
                while choice not in ["h", "s"]:
                    choice = input("Do you want to hit or stand? Please type h or s in order to proceed: ")

                if choice == "h":
                    self.__player_hand.add_card(self.__deck.deal_out())
                    self.__player_hand.adjust_for_ace()
                    self.print_game_state(is_endgame)
                else:
                    is_endgame = True
                    break

                if self.__player_hand.get_value() >= 21:
                    is_endgame = True
                    break

            while self.__computer_hand.get_value() < 17 and self.__player_hand.get_value() <= 21:
                self.__computer_hand.add_card(self.__deck.deal_out())
            self.print_game_state(is_endgame)
            self.win()

            continue_game = input("Do you want to continue? Y/N ")
            while continue_game.lower() not in ["y", "n"]:
                continue_game = input("Please enter Y or N ")
            if continue_game.lower() == "n":
                break
            self.reset()

game = Game()
game.start_game()
    

    

    
        