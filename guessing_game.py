"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
import random
import statistics


# Create the start_game function.
# Write your code inside this function.
def start_game(attempts_list=[]):
    keep_playing = True
    guesses = 0

    if attempts_list:
        print(f"Welcome! Curent High Score: {min(attempts_list)}")
    else:
        print(f"Welcome!")
    max_number = get_max_number()
    solution = random.randint(1, max_number)
    guess_limit = round((max_number / 20) + 3)
    print(f"You will receive {guess_limit} guesses")

    while keep_playing:
        try:
            choice = get_guess(max_number)
            guesses += 1
            if choice == solution:
                game_over('win', attempts_list, guesses)
            if guesses == guess_limit:
                keep_playing = game_over('lose', attempts_list, guesses)
                break
            player_feedback(guesses, guess_limit, choice, solution)

        except ValueError as e:
            print(f"Value Error: {e}")
        except:
            print(f"Unknown Error")
    exit()

def game_over(outcome, attempts_list, guesses):
    if outcome == 'win':
        print("Congratulations! You Won")
    attempts_list.append(guesses)
    display_data(attempts_list, guesses)

    play_again = input("Press 'Y' to play again:  ")
    if play_again.lower() == 'y':
        start_game(attempts_list=attempts_list)
    else:
        print("Goodbye")
        return False


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


def get_guess(max_number):
    while True:
        try:
            prompt = "Please guess a number:  "
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
        print(f"It's lower. Your choice of {choice} is too high \n{guesses_status} ")
    else:
        print(f"It's higher. Your choice of {choice} is too low \n{guesses_status}")



if __name__ == "__main__":
    start_game()

