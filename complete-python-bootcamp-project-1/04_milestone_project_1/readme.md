# Project: Tic Tac Toe Game - Player vs Player#

**How to start the game:** before runnning <pre>```python tic_tac_toe.py```</pre> in your terminal in the same directory as this file
(04_milestone_project_1).
Then install the required libraries using <pre>```pip install -r requirements.txt```</pre>.

**How to run tests:** run <pre>```pytest --cov=tic_tac_toe```</pre> in your terminal in the same directory as this file (04_milestone_project_1).

**How to play:** The game will prompt you to choose your mark (X or O). Then, players take turns entering their moves by specifying the position on the grid (1-9). The game will display the current board after each move. If a player tries to place their mark in an already occupied square, they will be prompted to try again. The game continues until one player wins or the game ends in a draw.

**How the code works:** You can find comprehensive documentaion in the code itself. 

**Output of the tests:**
<pre makrdown>
Name             Stmts   Miss  Cover
------------------------------------
tic_tac_toe.py      94      6    94%
------------------------------------
TOTAL               94      6    94%
</pre>

**Sample gameplay:**
```python

What do you want to choose? X or O. Type either X or O to choose: x
X's turn.
Enter your move from 1-9: 1
Current board:
 X | _ | _
---+---+---
 _ | _ | _
---+---+---
 _ | _ | _

Reference positions:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

O's turn.
Enter your move from 1-9: 2
Current board:
 X | O | _
---+---+---
 _ | _ | _
---+---+---
 _ | _ | _

Reference positions:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

X's turn.
Enter your move from 1-9: 5
Current board:
 X | O | _
---+---+---
 _ | X | _
---+---+---
 _ | _ | _

Reference positions:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

O's turn.
Enter your move from 1-9: 9
Current board:
 X | O | _
---+---+---
 _ | X | _
---+---+---
 _ | _ | O

Reference positions:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

X's turn.
Enter your move from 1-9: 9
That position has already been chosen!Try again! 
Enter your move from 1-9: 7
Current board:
 X | O | _
---+---+---
 _ | X | _
---+---+---
 X | _ | O

Reference positions:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

O's turn.
Enter your move from 1-9: 3
Current board:
 X | O | O
---+---+---
 _ | X | _
---+---+---
 X | _ | O

Reference positions:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

X's turn.
Enter your move from 1-9: 4
Current board:
 X | O | O
---+---+---
 X | X | _
---+---+---
 X | _ | O

Reference positions:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

X won!
Do you want to play again? Y/N n
Thanks for playing!
```