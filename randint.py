import random
number=random.randint(1,9)
no=0
while no!=number:
    noinput=input("Enter your guess:")
    no=int(noinput)
    if no<number:
        print("Too low!")
    elif no>number:
        print("Too high!")
print("Congrats!")