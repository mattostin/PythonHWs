import random 

def ask_user_for_int(prompt, low, high):
    while True:
        try:
            user_int = int(input(prompt))
            if low <= user_int <= high:
                return user_int
            else:
                print("Enter an integer between", low, "and", high)
        except ValueError:
            print("Enter an Integer Value")

def play_one_round():   
    global games_tied, games_won, computer_score
    
    user_choice = ask_user_for_int("Enter either 1 for rock, 2 for Paper, or 3 for Scissors: ", 1, 3)

    if user_choice == 1:
        print("You Chose Rock")
    elif user_choice == 2:
        print("You chose Paper")
    elif user_choice == 3:
        print("You Chose Scissors")
    else:
        print("INVALID INPUT TRY ENTERING A VALID NUMBER!")
        return
    
    computer_choice = random.randint(1, 3)

    if computer_choice == user_choice:
        print("You selected the same, It's a tie!")
        games_tied += 1
    elif (computer_choice == 1 and user_choice == 2):
            print("Computer chose Rock, YOU WIN!") 
            games_won += 1
    elif (computer_choice == 2 and user_choice == 3):
            print("Computer chose Paper, YOU WIN!") 
            games_won += 1
    elif (computer_choice == 3 and user_choice == 1):
            print("Computer chose Scissors, YOU WIN!")
            games_won += 1
    elif (computer_choice == 2 and user_choice == 1):
            print("Computer chose Paper, YOU LOSE!") 
            computer_score += 1
    elif (computer_choice == 3 and user_choice == 2):
           computer_score += 1
           print("Computer chose Scissors, YOU LOSE!") 
    elif (computer_choice == 1 and user_choice == 3):
            print("Computer chose Rock, YOU LOSE!")
            computer_score += 1

    

def main():
    global games_tied, games_won, computer_score
    games_won = 0
    games_tied = 0
    computer_score = 0

    num_played = ask_user_for_int("How many times would you like to play this game: ")

    for x in range(num_played):
        play_one_round()

    print("Computer Score:", computer_score)
    print("Your Score:", games_won)
    print("Number of ties:", games_tied)

if __name__ == "__main__":
    main()
