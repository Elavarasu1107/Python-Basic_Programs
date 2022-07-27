
def largest_number(number_one, number_two, number_three):
    """
    This function finds the largest value in the given parameters
    :param number_one: Integer values passed from main method
    :param number_two: Integer values passed from main method
    :param number_three: Integer values passed from main method
    :return: none
    """
    if number_one > number_two and number_one > number_three:
        print(number_one, " is the largest Number")
    elif number_two > number_one and number_two > number_three:
        print(number_two, " is the largest Number")
    else:
        print(number_three, " is the largest Number")


if __name__ == '__main__':
    number_one = int(input("Enter number one: "))
    number_two = int(input("Enter number two: "))
    number_three = int(input("Enter number three: "))
    largest_number(number_one, number_two, number_three)