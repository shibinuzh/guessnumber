import random

#To generate a random number
def generateRandomNumber(x, y):
    return random.randint(x, y)

#Logic of program
def guessNumber(number, x, y):
    guessedNumber=int(input(f"Guess number between {x} and {y}:"))
    #if guessed a number above
    if(guessedNumber > number):
        print("you guessed a number above")
        guessNumber(number, x, guessedNumber)
    #if guessed a number below 
    elif guessedNumber < number:
        print("you guessed a number below")
        guessNumber(number, guessedNumber, y)
    #if guessed the same number
    else:
        print("you did it!")
        print("you guessed the number")


#lower limit
x=1

#upper limit
y= 100

#Generating a number
random_number = generateRandomNumber(x, y)

#Function call
guessNumber(random_number, x, y)