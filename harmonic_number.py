def harmonic_number():
    """
    This function calculates the harmonic value upto n
    :return:
    """
    n = int(input("Enter the value of N: "))
    value = 0
    i = 1
    while i <= n:
        value = value + (1 / i)
        i += 1
    print("Harmonic value of a number: ", round(value, 3))


if __name__ == '__main__':
    harmonic_number()
