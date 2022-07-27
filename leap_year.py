
def leap_year():
    """
    This function used to find whether an entered year is leap year or not
    :return: none
    """
    year = int(input("Enter a Year: "))
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        print("Entered Year ", year, " is a Leap Year")
    else:
        print("Entered Year ", year, " is not a Leap Year")


if __name__ == '__main__':
    leap_year()
