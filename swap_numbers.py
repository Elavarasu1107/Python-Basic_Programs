
def swap():
    """
    This function swaps the two values entered by the user
    :return: none
    """
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    temp = a
    a = b
    b = temp
    print("Values after Swapping")
    print("A = ", a)
    print("B = ", b)


if __name__ == '__main__':
    swap()
