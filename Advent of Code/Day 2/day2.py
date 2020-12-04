# Written by Syed Muhammad Zafar Alam
# Coded in Python
# Dec. 04 / 2020

# open file
f = open("Advent of Code\Day 2\input.txt", "r")
f1 = f.readlines() # make a list of all lines
validpasses1 = 0 # counts part 1 
validpasses2 = 0 # counts part 2

for i in range(len(f1)):
    # get all variables from the specific line
    List = list(f1[i]) # make a list of all the characters in the line
    start = int("".join(List[0:List.index("-")]))
    end = int("".join(List[List.index("-")+1:List.index(" ")]))
    letter = List[List.index(" ")+1]
    password = "".join(List[List.index(":")+2:-1])
    lettercounter = 0 # counts # of times the letter appears in he password

    # part 1
    for character in password:
        if character == letter:
            lettercounter += 1
    
    if lettercounter >= start and lettercounter <= end:
        validpasses1 += 1

    # part 2
    if password[start-1] == letter and password[end-1] != letter or password[start-1] != letter and password[end-1] == letter: 
        validpasses2 += 1

print(validpasses1, validpasses2, sep="\n")