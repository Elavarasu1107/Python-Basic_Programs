
def vowels(letter):
    """
    This function determines whether the input character is a vowel or consonant
    :param letter: It's an input parameter from the user
    :return: none
    """
    letter = str.lower(letter)
    length = len(letter)
    if length == 1:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            print("Entered Alphabet is a vowel")
        else:
            print("Entered Alphabet is a Consonant")
    else:
        print("Enter a Single Digit Character")


if __name__ == '__main__':
    letter = input("Enter an Alphabet: ")
    vowels(letter)
