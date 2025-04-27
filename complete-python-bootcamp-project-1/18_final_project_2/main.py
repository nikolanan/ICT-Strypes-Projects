def colatz_conjecture_steps_number() -> int:
    """
    The Collatz conjecture is a sequence defined as follows:
    - Start with any positive integer n.
    - If n is even, divide it by 2.
    - If n is odd, multiply it by 3 and add 1.
    - Repeat the process indefinitely.
    The conjecture is that no matter what value of n, the sequence will always eventually reach 1.
    This function calculates the number of steps to reach 1 for a given positive integer n.
    :return: the number of steps to reach 1
    :rtype: int
    """
    while True:
        try:
            number = int(input("Enter a number equal or bigger than 1: "))
            if number < 1:
                continue
            break
        except ValueError:
            print("Only positive integers > 0 are accepted")
    counter = 0
    while True:
        if number == 1:
            return counter
        if number % 2 == 0:
            number = number//2
        else:
            number = number*3 + 1
        counter+=1

if __name__ == "__main__":
    NUMBER_OF_STEPS = colatz_conjecture_steps_number()
    print(f"The number of steps to reach 1 are: {NUMBER_OF_STEPS}")
