# %%
import itertools
import time
import numpy as np
import test_py
import test_cy


def read_word_files(solutions_path: str, guesses_path: str) -> tuple[list]:
    with open(solutions_path, "r") as solutions_file, open(guesses_path, "r") as guesses_file:
        solutions = sorted(solutions_file.read().split("\n"))
        guesses = sorted(guesses_file.read().split("\n") + solutions)
    return guesses, solutions


def generate_patterns() -> list[list]:
    ran = range(3)
    return list(itertools.product(ran, ran, ran, ran, ran))


solutions_path = "../Data/wordle_answers.txt"
guesses_path = "../Data/wordle_guesses.txt"

allowed_guesses, solutions = read_word_files(solutions_path, guesses_path)
patterns = generate_patterns()

# %%

#%timeit test_py.possible_words("trace", [0, 2, 2, 1, 2], np.array(allowed_guesses))

#%timeit test_cy.possible_words("trace", [0, 2, 2, 1, 2], allowed_guesses)

# %%

#%timeit test_py.exp_inf("trace", np.array(patterns), np.array(allowed_guesses))

#%timeit test_cy.exp_inf("trace", patterns, allowed_guesses)

# %%

#%timeit test_py.generate_exp_inf(np.array(["trace", "crane", "bipod", "ghoul", "sores"]), np.array(patterns), np.array(allowed_guesses))

# %timeit test_cy.generate_exp_inf(["trace", "crane", "bipod", "ghoul", "sores"], patterns, allowed_guesses)

# %%

start = time.perf_counter()
result = test_cy.generate_exp_inf(solutions, patterns, allowed_guesses)
elapsed = time.perf_counter() - start

print(f"Time required: {elapsed}")  # 5.74 min

# %%

data = np.array(result)

mean = np.mean(data)
mx   = np.max(data)
amx  = np.argmax(data)
mn   = np.min(data)
amn  = np.argmin(data)

print(f"Mean: {mean}, Max: {mx} ('{solutions[amx]}'), Min: {mn} ('{solutions[amn]}')")

# %%

start = time.perf_counter()
result = test_cy.generate_exp_inf(allowed_guesses, patterns, allowed_guesses)
elapsed = time.perf_counter() - start

print(f"Time required: {elapsed / 60:.2f} min")  # 31.83 min

with open("full_expectation.txt", "w") as f:
    for entry in result:
        f.write(str(entry) + "\n")

# %%

data = np.array(result)

mean = np.mean(data)
mx   = np.max(data)
amx  = np.argmax(data)
mn   = np.min(data)
amn  = np.argmin(data)

print(f"Mean: {mean}, Max: {mx} ('{allowed_guesses[amx]}'), Min: {mn} ('{allowed_guesses[amn]}')")

# %%
