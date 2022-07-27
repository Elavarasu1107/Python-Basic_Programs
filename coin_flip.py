import random


def coin_toss(user_input):
    """
    This functions calculates number of times head and tails flipped in the coin and its percentage
    :param user_input: It's a parameter passed from tha main method
    :return: none
    """
    no_of_heads = 0
    no_of_tails = 0
    i = 0
    while i < user_input:
        random_number = random.randint(0, 1)
        if random_number == 0:
            no_of_heads += 1
        else:
            no_of_tails += 1
        i += 1

    print("No of times head is flipped: ", no_of_heads)
    print("No of times tail is flipped: ", no_of_tails)
    heads_percentage = (no_of_heads * 100) / user_input
    tail_percentage = (no_of_tails * 100) / user_input
    print("Heads Percentage: ", heads_percentage)
    print("Tails Percentage: ", tail_percentage)


if __name__ == '__main__':
    user_input = int(input("Enter number of times coin to be flipped: "))
    coin_toss(user_input)
