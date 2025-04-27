def binary_or_decimal() -> str:
    """Decides if the user wants to convert binary to decimal or decimal to binary.

    :return: returns b for binary or d for decimal
    :rtype: str
    """
    while True:
        try:
            b_d = input("Enter d for decimal to binary or b for binary to decimal: ").lower()
            if b_d not in ["b", "d"]:
                print("Only d or b are accepted")
                continue
            return b_d
        except ValueError:
            print("Only d or b are accepted")

def convertor(b_d: str) -> int:
    """Converts binary to decimal or decimal to binary.
    The function takes a string input b_d, which indicates the conversion direction.

    :param b_d: The conversion direction: 'b' for binary to decimal, 'd' for decimal to binary.
    :type b_d: str
    :return: The converted number.
    :rtype: int
    """
    if b_d == "b":
        while True:
            try:
                number = input("Enter binary number: ")
                out_of_loop = True
                for i in number:
                    if i not in ["0", "1"]:
                        out_of_loop = False
                        print("Only 0 and 1 are accepted: ")
                        break
                if out_of_loop:
                    break
            except ValueError:
                print("Error")

        decimal_number = 0
        power_of_2 = len(number) - 1
        for digit in number:
            if digit != "0":
                decimal_number += 2**power_of_2
            power_of_2-=1
        return decimal_number

    while True:
        try:
            number = int(input("Enter decimal number: "))
            break
        except ValueError:
            print("You can enter only integer numbers")

    binary_number = ""
    while number >= 1:
        if (number % 10) % 2 == 0:
            binary_number += "0"
        else:
            binary_number += "1"
        number = number // 2
    binary_number = int(binary_number[::-1])
    return binary_number

if __name__ == "__main__":
    conversion_way = binary_or_decimal()
    print(convertor(conversion_way))
