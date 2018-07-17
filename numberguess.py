import random

numbers = [1,2,3,4,5,6,7,8,9,10]

def guess():
    n = random.choice(numbers)
    inp = int(input("Guess a number between 1 and 10:"))
    if (inp == n):
        print("You guessed it!")
        exit()
    if (inp > n):
        print("You were", inp-n, "over. Better luck next time!")
    if (inp < n):
        print("You were", n-inp, "under. Better luck next time!")

guess()
