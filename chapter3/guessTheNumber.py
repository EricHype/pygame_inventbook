#this is a guess the number game
import random


guessesTaken =0

print("Hello, what is your name?")
playerName = input()

number = random.randint(1, 20)
print("Well, " + playerName + " I am thinking of a number bewteen 1 and 20")

for guessesTaken in range(6):
    print("Take a guess")
    guess = input()
    guess = int(guess)

    if(guess < number):
        print("Your guess is too low")
    
    if(guess > number):
        print("Your guess is too high")

    if(guess == number):
        break

if(guess == number):
    guessesTaken = str(guessesTaken + 1)
    print("Good job, " + playerName + "! You got the answer in " + guessesTaken + " guesses!")
else:
    print("Nope! I was thinking of: " + str(number))