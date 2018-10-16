import random


def evaluate_guess(guess, target):
    """
    Determine weather the guess is correct or not and provide user feedback.
    """
    if guess == target:
        # Indicate that the user guessed correctly
        correct_guess = True
        message = 'Congrats! You guessed it.'
    elif guess > target:
        # Indicate that the user's guess is too high
        correct_guess = False
        message = 'Your guess is too high.'
    else:
        # Indicate that the user's guess is too low
        correct_guess = False
        message = 'Your guess is too low.'
    return correct_guess, message


def new_game(low, high, guess_count_max):
    """
    Start a new game.
    """
    # Generate the random number
    random_number = random.randint(low, high)

    # Initialize the guess count
    guess_count = 0

    # Start the loop, which terminates when the user guesses correctly or is out of guesses.
    while True:

        try:
            # Prompt the user for a guess and convert to an integer
            guess = int(input('--> Guess the number: '))
        except ValueError:
            # Continue to the next iteration if the user enters a non-number
            print('Invalid entry. Please try again.')
            print()
            continue

        # Add one to the guess count
        guess_count += 1

        # Determine whether the user guessed correctly and print feedback back to the terminal
        is_correct, feedback = evaluate_guess(guess, random_number)
        print(feedback)

        # End game if user guessed correctly loop
        if is_correct:
            break

        # End game if user is out of guesses
        if guess_count == guess_count_max:
            print("Game over. You're out of guesses :(")
            break

        # Print more feedback before the next guess
        print('Please try again. You have {} guesses remaining.'.format(guess_count_max - guess_count))
        print()


def main():
    """
    Play games until the user prompts to exit.
    """
    # Basic message telling the user how to play
    print()
    print('Welcome to Number Guesser! Try to guess the randomly generated number. Good luck!')

    # Start the loop, which terminates when the user prompts to exit
    while True:
        print()
        new_game(0, 100, 7)
        print()
        play_again = input('Would you like to play again? ([yes]/no): ')
        if play_again.lower() == 'no':
            break
        print('-----------------------------')


if __name__ == '__main__':
    main()
