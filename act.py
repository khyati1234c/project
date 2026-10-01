import random

low=int(input("enter lower limit"))
high=int(input("enter higher limit"))
comp=random.randint(low,high)

while(True):
    n=int(input("guess the number"))
    if n==comp:
        print("Correct")
        break

    elif n> comp:
        print("go lower")
    elif n< comp:
        print("go higher")