# Project: Collatz Conjecture Steps Counter

## How to start the program:

In your terminal, navigate to the directory containing the Python file (e.g., collatz_conjecture.py) and run:
```text
python main.py
```
No additional libraries are required.

## What the program does:

The Collatz Conjecture is a sequence defined as:

Start with any positive integer n.

If n is even, divide it by 2.

If n is odd, multiply it by 3 and add 1.

Repeat the process until n becomes 1.

This program asks the user for a starting number and calculates the number of steps needed to reach 1 following the Collatz Conjecture rules.

## Sample Input and Output:
### Example 1:
``` text
Enter a number equal or bigger than 1: 6
The number of steps to reach 1 are: 8
```
Explanation:
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (8 steps)

### Example 2:
``` text
Enter a number equal or bigger than 1: 19
The number of steps to reach 1 are: 20
```
Explanation:
19 → 58 → 29 → 88 → ... → 1 (20 steps)

### Example 3 (Invalid input handling):

``` text
Enter a number equal or bigger than 1: hello
Only positive integers > 0 are accepted
Enter a number equal or bigger than 1: -3
Only positive integers > 0 are accepted
Enter a number equal or bigger than 1: 7
The number of steps to reach 1 are: 16
```