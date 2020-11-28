#Written by Syed Muhammad Zafar Alam
#Coded in Python

def factorial_calculation(number):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    calculation = 1
    for i in range(4, number+1, 1):
        if i not in prime_numbers:
            calculation*= i
    return calculation

number = int(input())
print(factorial_calculation(number))