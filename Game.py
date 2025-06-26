import random

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def get_user_choice():
    choice = input("Enter your choice (stone/paper/scissors) or 'exit' to quit: ").lower()
    while choice not in ['stone', 'paper', 'scissors', 'exit']:
        print("Invalid input. Try again.")
        choice = input("Enter your choice (stone/paper/scissors) or 'exit' to quit: ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'stone' and computer == 'scissors') or \
         (user == 'paper' and computer == 'stone') or \
         (user == 'scissors' and computer == 'paper'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0
    print("🎮 Welcome to Stone Paper Scissors Game!")
    print("Type 'exit' anytime to stop playing.\n")

    while True:
        user_choice = get_user_choice()
        if user_choice == 'exit':
            break

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'tie':
            print("Result: It's a tie!\n")
        elif winner == 'user':
            print("Result: You win this round!\n")
            user_score += 1
        else:
            print("Result: Computer wins this round!\n")
            computer_score += 1


    print("\n🧾 Final Score:")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    if user_score > computer_score:
        print(" You are the overall winner!")
    elif computer_score > user_score:
        print(" Computer wins overall!")
    else:
        print(" It's an overall tie!")

play_game()
