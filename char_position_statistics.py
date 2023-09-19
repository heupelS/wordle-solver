#%%
from itertools import count
import numpy as np
import string


with open("Data/wordle_answers.txt", "r") as answers, open("Data/wordle_guesses.txt", "r") as guesses:
    allowed_guesses = np.append(np.array(answers.read().split("\n")), np.array(guesses.read().split("\n")))

#%%
def generate_patterns():
    patterns = []

    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    for e in range(3):
                        patterns.append([a, b, c, d, e])

    return np.array(patterns)
patterns = generate_patterns()

#%%

###################
alphabet = list(string.ascii_lowercase)


def generate_letter_pattern():
    letter_pattern = []
    for i in range(5):
        letter_pattern.append(alphabet)
    return np.array(letter_pattern)


def count_frequency_at_position(allowed_guesses):
    result = [[],[],[],[],[]]
    for i in range(5):
        for letter in alphabet:
            counter = 0
            for word in allowed_guesses:
                if (word[i] == letter):
                    counter += 1
            result[i].append(counter)
    return result




def determine_frequency_for_each_word(allowed_guesses):
    frequency = np.array(count_frequency_at_position(allowed_guesses))
    frequency = frequency/len(allowed_guesses)
    words_frequency_final = []
    for word in allowed_guesses:
        frequency_of_word = 0
        for i in range(5):
            for j in range(26):
                if (word[i] == alphabet[j]):
                    frequency_of_word += frequency[i][j]
        words_frequency_final.append(frequency_of_word)
    return words_frequency_final

#a = determine_frequency_for_each_word(allowed_guesses)

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




#%%
def probabilities_patterns(word, allowed_guesses):
    
    results = np.array([], dtype=int)

    for pat in patterns:
        count = 0

        for guess in allowed_guesses:
            for i in range(len(pat)):
                if word[i] in guess and pat[i] == 0: # plätze der vergleiche getauscht, da python lazy evaluated -> verbesserung laufzeit um 0,2s.
                    break
                elif (word[i] not in guess or word[i] == guess[i]) and pat[i] == 1:
                    break
                elif word[i] != guess[i] and pat[i] == 2:
                    break
            else:
                count += 1

        results = np.append(results, count)
    #print(results, np.sum(results))
    #print((np.average(results)))
    return np.sort(results)[::-1]





# %%
""" 
a.sort()
with open('a.txt', 'w') as f:
    for item in a:
        f.write("%s\n" % item)
 """
# %%
