# Implementation of a function reading txt files and of the game Wordle to be played by a human player in the console

import numpy as np


def read_word_files(solutions_path: str, guesses_path: str) -> tuple[list]:
    """
    Reads txt files which contain solution words and words which are allowed to be guessed and creates separate Numpy arrays containing these words.
    Note that it is assumed that the file containing the allowed guesses does *not* contain the solution words.

    Args:
        solutions_path (str): Path to txt file containing possible solution words
        guesses_path (str): Path to txt file containing words which are allowed to be guessed

    Returns:
        list: Numpy array containing words which are allowed to be guessed (sorted)
        list: Numpy array containing possible solution words (sorted)
    """

    with open(solutions_path, "r") as solutions_file, open(guesses_path, "r") as guesses_file:
        solutions = sorted(solutions_file.read().split("\n"))
        guesses = sorted(guesses_file.read().split("\n") + solutions)
    return guesses, solutions


"""
with open(solutions_path, "r") as solutions_file, open(guesses_path, "r") as guesses_file:
    solutions = np.sort(np.array(solutions_file.read().split("\n")))
    guesses = np.sort(np.append(solutions, np.array(guesses_file.read().split("\n"))))

return guesses, solutions
"""

def wordle(solutions: list, allowed_guesses: list, allowed_attempts: int, debug_print: bool) -> None:
    """
    Implementation of Wordle to be played by human players in the console.
    Convention regarding feedback given by the game for every guessed word:
        - 0 <-> letter not in solution ("gray")
        - 1 <-> letter in solution but at a different position ("yellow")
        - 2 <-> letter in solution at the correct position ("green")

    Args:
        solutions (list): Possible solution words
        allowed_guesses (list): Words which are allowed to be guessed by the player
        allowed_attempts (int): Number of attempts the player has to guess the solution
        debug_print (bool): Controls whether the solution word is printed in the beginning
    """

    # Choose a random word from the solution list and set the attempt counter equal to one
    solution = np.random.choice(solutions)
    attempt = 1

    if debug_print:
        print(solution)

    # while-else clause: the else statement is executed if and only if the while condition becomes false (i.e. it is not executed iff the while loop breaks)
    while attempt < allowed_attempts + 1:

        guess = input(f"{attempt}. attempt: ")

        if guess not in allowed_guesses:

            print("Invalid guess! Try again.")
            continue

        elif guess == solution:

            print(f"You have won! The word '{guess}' is correct.")
            return

        else:

            # Create array which will encode feedback for every letter in guess
            feedback = []

            for i, letter in enumerate(guess):

                # Case 1: Letter at correct position
                if letter == solution[i]:
                    feedback.append((letter, 2))

                # Case 2: Letter in word but at a different position
                elif letter in solution:
                    feedback.append((letter, 1))

                # Case 3: Letter not in word
                else:
                    feedback.append((letter, 0))

            # Print feedback and increment attempt
            print(feedback)
            attempt += 1

    # If while loop finishes without break, the game has been lost
    else:
        print(f"You have lost! The correct word was '{solution}'.")


if __name__ == "__main__":
    # Paths to solution words and allowed guesses
    solutions_path = "Data/wordle_answers.txt"
    guesses_path = "Data/wordle_guesses.txt"

    # Read files and create lists containing solution words and allowed guesses
    allowed_guesses, solutions = read_word_files(solutions_path, guesses_path)

    # Play Wordle
    wordle(solutions, allowed_guesses, 6, False)
