import random

number_guessed=random.randrange(100)

print("new game")

number_of_chance=3

guessed=0

while guessed > number_of_chance:
    guessed+=1
    n=int(input("enter the number:"))
    
    if n==number_guessed:
        print("u guessed right")
        break
    elif(guessed>=number_guessed and n!=number_guessed):
        print(f"chance is over and the number is {number_guessed}")
    elif n>number_guessed:
        print("the number is high")
    elif n<number_guessed:
        print("the number is lower")