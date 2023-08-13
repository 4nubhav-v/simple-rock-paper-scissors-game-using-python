import random

print("??????????????????Welcome to Rock Paper Scissors game?????????????\n")
a = (
    input(
        "Enter 'Rock' for choosing rock or \nEnter 'Paper' for choosing paper or \nEnter 'Scissors' for choosing scissors "
    )
).lower()
n = ["rock", "paper", "scissors"]
ran = n[random.randint(0, 2)]
if ran == a:
    print("Draw")
elif ran == "rock":
    print("Computer choosed 'Rock' ")
    if a == "paper":
        print("You win :)")
    else:
        print("You lose :(")
elif ran == "paper":
    print("Computer choosed 'Paper' ")
    if a == "scissors":
        print("You win :)")
    else:
        print("You lose :(")
else:
    print("Computer choosed 'Scissors' ")
    if a == "rock":
        print("You win :)")
    else:
        print("You lose :(")
