import math


def possible_words(word: str, pattern: list, guesses: list[str]) -> list:
    possible_solutions = []
    for guess in guesses:
        for i, color in enumerate(pattern):
            if word[i] in guess and color == 0:
                break
            elif (word[i] not in guess or word[i] == guess[i]) and color == 1:
                break
            elif word[i] != guess[i] and color == 2:
                break
        else:
            possible_solutions.append(guess)
    return possible_solutions


def exp_inf(word: str, patterns: list, allowed_guesses: list) -> float:
    omega = len(allowed_guesses)
    var = 0
    for pat in patterns:
        p = len(possible_words(word, pat, allowed_guesses)) / omega
        if p == 0.0:
            continue
        else:
            var += p * math.log2(p)
    return - var


def generate_exp_inf(words: list, patterns: list, allowed_guesses: list) -> float:
    results = []
    for w in words:
        val = exp_inf(w, patterns, allowed_guesses)
        results.append(val)
    return results
