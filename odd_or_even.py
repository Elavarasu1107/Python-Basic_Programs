def odd_or_even(user_input):
    """
    This function find whether given number is an Odd or Even
    :param user_input: Integer value passed from the main method
    :return: none
    """
    if user_input % 2 == 0:
        print("Entered Number is a Even Number")
    else:
        print("Entered Number is a Odd Number")


if __name__ == '__main__':
    user_input = int(input("Enter a Number: "))
    odd_or_even(user_input)
