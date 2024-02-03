import random

num_1 = int(input("Enter either 1 for rock, 2 for Paper, or 3 for Scissors: "))

if num_1 == 1:
    print("You Chose Rock")
elif num_1 == 2:
    print("You chose Paper")
elif num_1 == 3:
    print("You Chose Scissors")
else:
    print("Invalid Choice, pick one of the provided options")
    exit()


computer_choice = random.randint(1, 3)

if(computer_choice == 1 and num_1 == 1):
    print("The computer chose rock and so did you, TIE!")
if(computer_choice == 2 and num_1 == 2):
    print("The computer chose Paper and so did you, TIE!")
if(computer_choice == 3 and num_1 == 3):
    print("The computer chose Scissors and so did you, TIE!")
if(computer_choice == 2 and num_1 == 1):
    print("The computer chose paper YOU LOSE!")
if(computer_choice == 2 and num_1 == 3):
    print("The computer chose paper YOU WIN!")
if(computer_choice == 3 and num_1 == 1):
    print("The computer chose scissors YOU LOSE!")
if(computer_choice == 3 and num_1 == 2):
    print("The computer chose scissors YOU LOSE!")
if(computer_choice == 1 and num_1 == 2):
    print("The computer chose rock YOU WIN!")
if(computer_choice == 1 and num_1 == 2):
    print("The computer chose rock YOU WIN!")
