
def power_table():
    """
    This function calculates the value 2 to the power of n
    :return: none
    """
    base_value = 2
    n = int(input("Enter the value of n: "))
    i = 1
    while i <= n:
        result = base_value ** i
        print(result, end=" ")
        i += 1


if __name__ == '__main__':
    power_table()
    