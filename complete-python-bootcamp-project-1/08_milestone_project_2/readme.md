# Project: Blackjack Game agains a computer dealer

## Description
This is a simple command-line Blackjack game implemented in Python. The game allows a single player to compete against a computer dealer. The objective is to get as close to 21 as possible without exceeding it, while also beating the dealer's hand.

## Features
- Simulates a standard deck of 52 playing cards.
- Implements basic Blackjack rules, including hitting, standing, and busting.
- Handles Ace values dynamically as 1 or 11.
- Includes betting functionality with a starting balance.
- Provides clear instructions and feedback during gameplay.

## How to Play
1. Run the script to start the game.
2. Place your bet at the beginning of each round.
3. Choose to "Hit" to draw another card or "Stand" to end your turn.
4. The dealer will play according to standard rules.
5. The winner is determined based on the final hand values.

## Requirements
No requirements are needed to run this script. It uses only built-in Python libraries, but for the tests, you need to install the following library:
 <pre>```pip install -r requirements.txt```</pre>

## How to run the game
Run the following command in your terminal in the same directory as this file (08_milestone_project_2):
 <pre>```python blackjack.py```</pre>

## How to run the tests
run the tests in your terminal in the same directory as this file (08_milestone_project_2) with:
 <pre>```pytest --cov=blackjack --cov-report=term```</pre>

## Find comprehensive documentation in the code itself
The code is well-commented and includes docstrings for all functions and classes, explaining their purpose and usage.

## Test Coverage
<pre markdown>
Name           Stmts   Miss  Cover
----------------------------------
blackjack.py     153      7    95%
----------------------------------
TOTAL            153      7    95%
</pre>

## Sample Gameplay
```text
Your current amount is 100
Please enter your bet: 100
Dealer has:
_
Eight of Diamonds
You have:
Three of Diamonds
Three of Clubs
Do you want to hit or stand? Type h or s: h
Dealer has:
_
Eight of Diamonds
You have:
Three of Diamonds
Three of Clubs
Four of Diamonds
Do you want to hit or stand? Type h or s: h
Dealer has:
_
Eight of Diamonds
You have:
Three of Diamonds
Three of Clubs
Four of Diamonds
Ten of Clubs
Do you want to hit or stand? Type h or s: s
Dealer has:
Seven of Spades
Eight of Diamonds
Five of Diamonds
You have:
Three of Diamonds
Three of Clubs
Four of Diamonds
Ten of Clubs

Final Hands:
Dealer: 20
Player: 20
It's a tie! Bet returned.
Do you want to continue? Y/N y
Your current amount is 100.0
Please enter your bet: 50
Dealer has:
_
Six of Hearts
You have:
Two of Spades
Three of Hearts
Do you want to hit or stand? Type h or s: h
Dealer has:
_
Six of Hearts
You have:
Two of Spades
Three of Hearts
King of Spades
Do you want to hit or stand? Type h or s: h
Dealer has:
_
Six of Hearts
You have:
Two of Spades
Three of Hearts
King of Spades
Six of Clubs
Dealer has:
Two of Diamonds
Six of Hearts
Nine of Clubs
You have:
Two of Spades
Three of Hearts
King of Spades
Six of Clubs

Final Hands:
Dealer: 17
Player: 21
Congrats! You win 100.0
Do you want to continue? Y/N y
Your current amount is 150.0
Please enter your bet: 100
Dealer has:
_
Ace of Diamonds
You have:
Nine of Hearts
Jack of Diamonds
Do you want to hit or stand? Type h or s: h
Dealer has:
_
Ace of Diamonds
You have:
Nine of Hearts
Jack of Diamonds
Nine of Spades
Dealer has:
Ten of Hearts
Ace of Diamonds
You have:
Nine of Hearts
Jack of Diamonds
Nine of Spades

Final Hands:
Dealer: 21
Player: 28
You busted! Dealer wins.
Do you want to continue? Y/N n
```


