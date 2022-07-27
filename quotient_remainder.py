
def quotient_remainder(divident, divisor):
    """
    This function calculates quotient and remainder
    :param divident: It is an input parameter passed from the main method by the user
    :param divisor: It is an input parameter passed from the main method by the user
    :return: none
    """
    print("Quotient: ", divident / divisor)
    print("Remainder: ", divident % divisor)


if __name__ == '__main__':
    divident = int(input("Enter the value of Divident: "))
    divisor = int(input("Enter the value of Divisor: "))
    quotient_remainder(divident, divisor)