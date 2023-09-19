# %%
import random
import numpy as np
from wordle import read_word_files
from statistics_words import check_compatibility_word_pattern, generate_patterns


def check1(guess: str, word: str, pattern: list) -> bool:
    check_compatibility_word_pattern(guess, word, pattern)

def check2(guess: str, word: str, pattern: list) -> bool:
    for i, color in enumerate(pattern):
        if word[i] in guess and color == 0:
            return False
        elif (word[i] not in guess or word[i] == guess[i]) and color == 1:
            return False
        elif word[i] != guess[i] and color == 2:
            return False
    else:
        return True


def check_p1(word, patterns):
    results = np.array([], dtype=int)
    for pat in patterns:
        count = 0
        for guess in allowed_guesses:
            for i in range(len(pat)):
                if pat[i] == 0 and word[i] in guess:
                    break
                elif pat[i] == 1 and (word[i] not in guess or word[i] == guess[i]):
                    break
                elif pat[i] == 2 and word[i] != guess[i]:
                    break
            else:
                count += 1
        results = np.append(results, count)
    return np.sort(results)[::-1]


def check_p2(word, patterns):
    results = np.array([], dtype=int)
    for pat in patterns:
        count = 0
        for guess in allowed_guesses:
            for i in range(len(pat)):
                if word[i] in guess and pat[i] == 0:
                    break
                elif (word[i] not in guess or word[i] == guess[i]) and pat[i] == 1:
                    break
                elif word[i] != guess[i] and pat[i] == 2:
                    break
            else:
                count += 1
        results = np.append(results, count)
    return np.sort(results)[::-1]


solutions_path = "Data/wordle_answers.txt"
guesses_path = "Data/wordle_guesses.txt"
allowed_guesses, _ = read_word_files("Data/wordle_answers.txt", "Data/wordle_guesses.txt")

patterns = generate_patterns()

# %%
