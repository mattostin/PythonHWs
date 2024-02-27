import random 
import time


while True:

    
    num_1 = int(input("Enter either 1 for rock, 2 for Paper, or 3 for Scissors: "))
    if num_1 == 1:
        print("You Chose Rock")
    elif num_1 == 2:
        print("You chose Paper")
    elif num_1 == 3:
        print("You Chose Scissors")
    else:
     print("INVALID INPUT TRY ENTERING A VALID NUMBER!")
     continue

    time.sleep(1)
    print("Computer is thinking...")
    time.sleep(2.5)
    
    computer_choice = random.randint(1, 3)

    if computer_choice == num_1:
        print("You selected the same, It's a tie!")
    elif (computer_choice == 1 and num_1 == 2):
        print("Computer chose Rock, YOU WIN! ")
        break
    elif (computer_choice == 2 and num_1 == 3):
        print("Computer chose Paper, YOU WIN!")
        break
    elif (computer_choice == 3 and num_1 == 1):
        print("Computer chose Scissors, YOU WIN!")
        break
    else:
        if (computer_choice == 1 and num_1 == 3):
            print("Computer chose Rock, YOU LOSE!")
        if (computer_choice == 2 and num_1 == 1):
            print("Computer chose Paper, YOU LOSE!")
        if (computer_choice == 3 and num_1 == 2):
            print("Computer chose Scissors, YOU LOSE!")
   
