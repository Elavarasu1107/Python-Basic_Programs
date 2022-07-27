
def prime_factor():
    """
    This function prints the prime factors of an input
    :return: none
    """
    least_prime_number = 2
    n = int(input("Enter a value of N: "))
    while least_prime_number <= n:
        if n % least_prime_number == 0:
            initial_value = least_prime_number
            print(initial_value, end=" ")
            n /= least_prime_number
        else:
            least_prime_number += 1


if __name__ == '__main__':
    prime_factor()
