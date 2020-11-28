# Written by Syed Muhammad Zafar Alam
# Coded in Python 
# Nov. 27/2020


# checks if number's length is 10 digits
def length(number):
    if len(number)==10:
        return True
    return False

# main function
def spam_or_not(number):
    start = ["800", "909"]

    # runs exception loop
    while (length(number)!=True):
        try:
            raise BaseException
        except:
            print("Please enter a ten digit number: ")
            number = input()

    # checks for requirements
    if number[:3] in start or (number[3] == number[4] and number[3] == number[5]) or (number[:5:-1] == number[6:]):
        return "yes"
    return "no"

number = input("Enter a ten-digit number: ")

print(spam_or_not(number))