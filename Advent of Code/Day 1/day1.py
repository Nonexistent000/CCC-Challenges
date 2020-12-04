# Written by Syed Muhammad Zafar Alam
# Coded in Python
# Dec. 04 / 2020

# open file
with open("Advent of Code\Day 1\input.txt", "r") as f:
    f1 = f.readlines() # make a list of all numbers
    f2 = f1[1:] # make a list of all numbers except the first one
    f3 = f2[1:] # make a list of all numbers except the first and second ones

# part 1
for i in range(len(f1)):
    num1 = int(f1[i])
    for j in range(len(f2)):
        num2 = int(f2[j])
        if num1 + num2 == 2020:
            print(num1*num2)
            break
        else:
            continue

# part 2
for i in range(len(f1)):
    num1 = int(f1[i])
    for j in range(len(f2)):
        num2 = int(f2[j])
        for k in range(len(f3)):
            num3 = int(f3[k])
            if num1 + num2 + num3 == 2020:
                print(num1*num2*num3)
                break
            else:
                continue