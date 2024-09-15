# Doesn't work quite right yet..
import random


num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number:"))

if (n == num):
    print("Great! You guess the number on the first try!! You're a MASTERMIND!")
else:
    ctr = 0

    while (n != num):
        ctr += 1
        
        count = 0


        n = str(n)

        num = str(num)

        correct = ['X'] * 4


        for i in range(0, 10):
            if (n[i] == num[i]):
                count += 1
                correct[i] = n[i]
            else:
                continue
        


        print("Not quite the number. But you did get ", count, " digit(s) correct!")
        print('\n')
        print('\n')
        n = int(input("Enter your next choice of numbers: "))

    if (count == 0):
        print("None of the numbers in your input match.")
        n = int(input("Enter your next choice of numbers: "))
        
    

if n == num:
    ctr += 1
    print("You've become a Mastermind!")
    print("It only took you", ctr, "tries...")

else:
    print("I don't know exactly what you've done...")
    
