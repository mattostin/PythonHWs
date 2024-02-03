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

print("The computer chose:")

computer_choice = random.randint(1, 3)


if num_1 == computer_choice:
    print("You tied")
elif (num_1 == 1 and computer_choice == 3) or (num_1 == 2 and computer_choice == 1) or (num_1 == 3 and computer_choice == 2):
    print("You won")
else:
    print("You lost")
