import copy
import numpy as np
import char_position_statistics
import wordle_main


def wordle_solver(allowed_attempts: int, allowed_guesses: list, full_expectation: list):
    # Print top 5 start guesses
    patterns = char_position_statistics.generate_patterns()
    phase_space = copy.deepcopy(allowed_guesses)
    attempt = 1
    while attempt < allowed_attempts + 1:
        word = input(f"{attempt}. word: ")
        pattern = input(f"{attempt}. pattern: ")
        pattern = [int(w) for w in pattern]

        red_pp = char_position_statistics.possible_words(word, pattern, allowed_guesses)
        exp_inf = char_position_statistics.determine_frequency_for_each_word(red_pp)

        max_exp_inf = np.max(exp_inf)
        ind_max_exp_inf = np.argmax(exp_inf)

        best_word = red_pp[ind_max_exp_inf]

        allowed_guesses = red_pp

        if max_exp_inf == -0.0:
            print(f"Only choice: {best_word}. (expected information = 0) --> You have won!")
        else:
            print(f"Best choice: {best_word}. (expected information = {max_exp_inf})")

        attempt += 1


if __name__ == "__main__":
    solutions_path = "Data/wordle_answers.txt"
    guesses_path = "Data/wordle_guesses.txt"

    allowed_guesses, solutions = wordle_main.read_word_files(solutions_path, guesses_path)

    wordle_solver(6, allowed_guesses, [])
