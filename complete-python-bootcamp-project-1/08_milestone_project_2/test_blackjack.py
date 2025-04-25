from blackjack import Card, Deck, Balance, Hand, Game, suits, ranks, values

def test_card():
    """
    Tests the Card class to ensure it initializes correctly with suit, rank, and value.
    """
    card = Card("Hearts", "Ace", 11)
    assert card.get_suit() == "Hearts", "Card suit should be 'Hearts'"
    assert card.get_rank() == "Ace", "Card rank should be 'Ace'"
    assert card.get_value() == 11, "Card value should be 11"

def test_deck():
    """
    Tests the Deck class to ensure it initializes correctly.
    """
    deck = Deck()
    assert deck.deck_length() == 52, "Deck should contain 52 cards"
    card = deck.deal_out()
    assert isinstance(card, Card), "First element should be a Card instance"
    assert deck.deck_length() == 51, "Deck should contain 51 cards after dealing one"
    assert card.get_suit() in suits, "Card suit should be one of the defined suits"
    assert card.get_rank() in ranks, "Card rank should be one of the defined ranks"
    assert card.get_value() in values.values(), "Card value should be one of the defined values"
    deck1 = Deck()
    deck2 = Deck()
    deck1.shuffle()
    assert print(deck1.deck_length()) == print(deck2.deck_length()), "Decks should be equal in length after shuffle"
    assert str(deck1) != str(deck2), "Shuffled decks should not be equal"

def test_balance():
    """
    Tests the Balance class and its methods.
    """
    balance = Balance()
    assert balance.get_balance() == 100, "Initial balance should be 0"
    assert balance.widraw(150) is False, "Should not be able to withdraw more than balance"
    balance.add_funds(100)
    assert balance.get_balance() == 200, "Balance should be 100 after adding funds"
    assert balance.widraw(50) is True, "Should be able to withdraw 50 from balance"
    assert balance.get_balance() == 150, "Balance should be 50 after withdrawal"

def test_hand():
    """
    Tests the hand class and its methods.
    """
    hand = Hand()
    hand.add_card(Card("Hearts", "Ace", 11))
    assert len(hand.get_cards()) == 1, "Hand should contain 1 card after adding one"
    assert hand.get_value() == 11, "Hand value should be 11 after adding Ace"
    hand.add_card(Card("Hearts", "Ace", 11))
    hand.adjust_for_ace()
    assert hand.get_value() == 12, "Hand value should be 12 after adjusting for Ace"

def test_game_initialization():
    game = Game()
    
    assert isinstance(game._Game__player_hand, Hand), "Player hand should be initialized as a Hand object"
    assert isinstance(game._Game__computer_hand, Hand), "Computer hand should be initialized as a Hand object"
    assert isinstance(game._Game__deck, Deck), "Deck should be initialized as a Deck object"
    assert game._Game__deck.deck_length() == 52, "Deck should contain 52 cards initially"
    assert isinstance(game._Game__balance, Balance), "Balance should be initialized as a Balance object"


def test_game_place_bet(monkeypatch):
    """
    Tests the place_bet method to ensure it correctly handles user input for betting.
    """
    game = Game()
    user_inputs = iter(["110","1000","33fss","100"])
    monkeypatch.setattr("builtins.input",lambda _: next(user_inputs))
    game.place_bet()
    assert game._Game__balance.get_balance() == 0

from unittest.mock import MagicMock

def test_game_win(capsys):
    """
    Tests the win method to ensure the correct winner is determined based on the hands.
    """
    game = Game()
    
    game._Game__player_hand = MagicMock()
    game._Game__computer_hand = MagicMock()

    game._Game__player_hand.get_value.return_value = 22  
    game._Game__computer_hand.get_value.return_value = 18  
    
    game.win()  
    # Check that the expected print statement is shown
    assert "You busted! Dealer wins." in capsys.readouterr().out
    
    # Test case where dealer busts
    game._Game__player_hand.get_value.return_value = 18
    game._Game__computer_hand.get_value.return_value = 22  

    game.win()
    assert "Dealer busted! You win!" in capsys.readouterr().out

    # Test case where player wins
    game._Game__player_hand.get_value.return_value = 20
    game._Game__computer_hand.get_value.return_value = 18

    game.win()
    assert "Congrats! You win" in capsys.readouterr().out

    # Test case where dealer wins
    game._Game__player_hand.get_value.return_value = 18
    game._Game__computer_hand.get_value.return_value = 20

    game.win()
    assert "You lost." in capsys.readouterr().out

    # Test case where it's a tie
    game._Game__player_hand.get_value.return_value = 20
    game._Game__computer_hand.get_value.return_value = 20

    game.win()
    assert "It's a tie! Bet returned." in capsys.readouterr().out

def test_print_game_state(capsys):
    """
    Tests the print_game_state method to ensure it correctly displays the game state.
    """
    game = Game()

    game = Game()
    
    game._Game__player_hand = MagicMock()
    game._Game__computer_hand = MagicMock()

    game._Game__player_hand.get_cards.return_value = ["Ace of Spades", "10 of Hearts"]
    game._Game__computer_hand.get_cards.return_value = ["2 of Diamonds", "King of Clubs"]

    # Test when it's not the end of the game
    game.print_game_state(False)
    captured = capsys.readouterr()  # Capturing thee output
    assert "Dealer has:" in captured.out
    assert "_" in captured.out  # hidden in output
    assert "You have:" in captured.out
    assert "Ace of Spades" in captured.out

    # Test when it's the end of the game
    game.print_game_state(True)
    captured = capsys.readouterr()  
    assert "Dealer has:" in captured.out
    assert "2 of Diamonds" in captured.out
    assert "You have:" in captured.out
    assert "Ace of Spades" in captured.out

def test_game_reset():
    """
    Tests the reset method to ensure the game state is reset correctly.
    """
    game = Game()

    game._Game__player_hand = MagicMock()
    game._Game__computer_hand = MagicMock()
    game._Game__deck = MagicMock()

    game._Game__bet = 100
    game._Game__player_hand.get_value.return_value = 20
    game._Game__computer_hand.get_value.return_value = 18
    game._Game__deck.deck_length.return_value = 9
    
    game.reset()
    assert game._Game__bet == 0
    assert game._Game__deck.deck_length() == 52
    assert isinstance(game._Game__player_hand, Hand)
    assert isinstance(game._Game__computer_hand, Hand)
    assert isinstance(game._Game__deck, Deck)


    game._Game__player_hand = MagicMock()
    game._Game__computer_hand = MagicMock()
    game._Game__deck = MagicMock()

    game._Game__bet = 100
    game._Game__player_hand.get_value.return_value = 20
    game._Game__computer_hand.get_value.return_value = 18
    game._Game__deck.deck_length.return_value = 32
    game.reset()
    assert game._Game__deck.deck_length() != 52
    assert isinstance(game._Game__player_hand, Hand)
    assert isinstance(game._Game__computer_hand, Hand)

def test_start_game_one_round(monkeypatch):

    game = Game()
    game.place_bet = MagicMock()
    game.win = MagicMock()
    mock_card = MagicMock()
    mock_deck = MagicMock()
    mock_deck.deal_out.return_value = mock_card
    game._Game__deck = mock_deck

    mock_player_hand = MagicMock()
    mock_dealer_hand = MagicMock()

    mock_player_hand.get_value.side_effect = [10, 18, 18]  # hit, after hit, after dealer
    mock_player_hand.adjust_for_ace = MagicMock()
    mock_player_hand.add_card = MagicMock()
    mock_player_hand.get_cards.return_value = [mock_card, mock_card]

    mock_dealer_hand.get_value.side_effect = [10, 16, 18]
    mock_dealer_hand.add_card = MagicMock()
    mock_dealer_hand.get_cards.return_value = [mock_card, mock_card]

    game._Game__player_hand = mock_player_hand
    game._Game__computer_hand = mock_dealer_hand

    game.print_game_state = MagicMock()

    inputs = iter(["h", "s", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game.start_game()

    assert game.place_bet.called
    assert mock_player_hand.add_card.call_count >= 1
    assert mock_player_hand.adjust_for_ace.called
    assert game.win.called
