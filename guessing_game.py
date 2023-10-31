"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
import random
import statistics


def main_menu(attempts_list):
    while True:
        choice = get_menu_choice()
        if choice == 1:
            attempts_list = start_game(attempts_list)
        elif choice == 2:
            print("Thanks for playing! Goodbye")
            break


def start_game(attempts_list):
    keep_playing = True
    guesses = 0

    if len(attempts_list) > 0:
        print(f"\nLet's begin! Current High Score: {min(attempts_list)}")
    else:
        print(f"\nLet's begin!")
    max_number = get_max_number()
    solution = random.randint(1, max_number)
    guess_limit = round((max_number / 20) + 3)
    print(f"You will receive {guess_limit} guesses\n")

    while keep_playing:
        try:
            choice = get_guess(max_number)
            guesses += 1
            if choice == solution:
                updated_attempts_list = game_over('win', attempts_list, guesses)
                return updated_attempts_list
            if guesses == guess_limit:
                updated_attempts_list = game_over('lose', attempts_list, guesses)
                return updated_attempts_list
            player_feedback(guesses, guess_limit, choice, solution)

        except ValueError as e:
            print(f"Value Error: {e}")
        except:
            print(f"Unknown Error")
    exit()

def game_over(outcome, attempts_list, guesses):
    if outcome == 'win':
        print("Congratulations! You Won")
    else:
        print("Sorry - Too many incorrect guesses. Game Over.")
    attempts_list.append(guesses)
    display_data(attempts_list, guesses)
    return attempts_list


def display_data(attempts_list, guesses):
    display = f"""
    Your Current Game Results:
    Guesses: {guesses}
    Mean: {statistics.mean(attempts_list)}
    Median: {statistics.median(attempts_list)}
    Mode: {statistics.mode(attempts_list)}   
    Minimum: {min(attempts_list)}
    Maximum: {max(attempts_list)}
    All Attempts: {attempts_list}
    """
    print(display)


def get_max_number():
    while True:
        try:
            max_number = int(input("What is the max number you would like to guess to: 1 to "))
            if max_number > 0:
                return max_number
            else:
                raise ValueError
        except:
            print("Please enter an integer greater than 0")


def get_menu_choice():
    while True:
        try:
            print("\nWelcome to the Number Guessing Game")
            print("1 to Play")
            print("2 to Exit")
            choice = int(input("Choose an option (1/2): "))
            if choice == 1 or choice == 2:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Please enter an integer of 1 or 2")

def get_guess(max_number):
    while True:
        try:
            prompt = f"Please guess a number between 1 and {max_number}:  "
            choice = int(input(prompt))
            if choice <= 0:
                raise ValueError("Out of Range: Number must be greater than 0")
            if choice > max_number:
                raise ValueError(f"Out of Range: Number must be less than or equal to {max_number}")
            return choice
        except ValueError:
            print(f"Value Error: Number must be an Integer between 1 and {max_number}")
        except:
            print("Unknown Error")


def player_feedback(guesses, guess_limit, choice, solution):
    guesses_status = f"Guesses Used: {guesses}  | Guesses Remaining: {guess_limit - guesses}"
    if choice > solution:
        print(f"\nIt's lower. Your choice of {choice} is too high \n{guesses_status} ")
    else:
        print(f"\nIt's higher. Your choice of {choice} is too low \n{guesses_status}")



if __name__ == "__main__":
    main_menu([])

