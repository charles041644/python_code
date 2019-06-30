## version 2: Not Correct
import random
cmp = random.randint(1, 100)

guess = input("Guess a number between 1 and 100: ")

while not guess.isdigit():
    guess = input("Wrong input, Please input a number: ")

guess = int(guess)
while guess > 100 or guess < 1:
    guess = input("The number must between 1-100: ")

if(cmp == guess):
    print("Correct!!")
elif(cmp > guess):
    print("Guess a large number")
else: 
    print("Guess a small number")
