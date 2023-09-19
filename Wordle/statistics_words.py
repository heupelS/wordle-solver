
#%%
import numpy as np
from wordle import read_word_files


def generate_patterns() -> list[list]:
    """
    Generates possible patterns which can occur when a word is entered into Wordle.
    (Corresponds to drawing five times from an urn with three distinct objects considering the permutation of them and putting them back after each draw; in total, there are 3**5 = 243 different possibilities.)
    Convention regarding content of patterns:
        - 0 <-> letter not in solution ("gray")
        - 1 <-> letter in solution but at a different position ("yellow")
        - 2 <-> letter in solution at the correct position ("green")

    # Possible Numpy implementation: np.sort(np.array(np.meshgrid(range(3), range(3), range(3), range(3), range(3), copy=False, indexing="ij")).T.reshape(-1,5))

    Returns:
        list: Collection containing every pattern as a five-element list
    """

    ran = range(3)
    patterns = [[a, b, c, d, e] for a in ran for b in ran for c in ran for d in ran for e in ran]

    return np.array(patterns)


def check_compatibility_word_pattern(guess: str, word: str, pattern: list) -> bool:
    """
    Checks whether a given word 'guess' is compatible with a pattern corresponding to a word 'word' which was given as feedback from Wordle.

    Args:
        guess (str): Word whose compatibility whith a pattern shall be checked
        word (str): Word that was used to generate the pattern (i.e. the colors of the pattern are related to this word)
        pattern (list): Pattern against which guess will be checked for compatibility encoded as five-element list containing 0, 1, 2

    Returns:
        bool: Is guess compatible with pattern
    """

    # Loop through each position in the given pattern
    # for-else clause: else statement is executed if and only if for loop finishes (i.e. it is not executed iff the for loop breaks)
    for i, color in enumerate(pattern):

        # Case 1: Letter at position 'i' of word is not correct but guess contains this letter
        if word[i] in guess and color == 0:
            return False

        # Case 2: Letter at position 'i' of word is at a different position, but guess does not contain this letter or guess does contain this letter at position i
        elif (word[i] not in guess or word[i] == guess[i]) and color == 1:
            return False

        # Case 3: Letter at position 'i' of word is correct but guess does not contain letter at this position
        elif word[i] != guess[i] and color == 2:
            return False

    # If for loop finishes without break, guess is a possible solution
    else:
        return True


def vectorized_check_compatibility_word_pattern(guesses: list, word: str, pattern: list) -> list[bool]:
    """
    Vectorized 'check_compatibility_word_pattern'

    Args:
        guesses (list): List of words whose compatibility whith a pattern shall be checked
        word (str): Word that was used to generate the pattern (i.e. the colors of the pattern are related to this word)
        pattern (list): Pattern against which guess will be checked for compatibility encoded as five-element list containing 0, 1, 2

    Returns:
        list: Is guess compatible with pattern
    """

    # Generate vectorized function for 'word' and 'pattern' which then only takes a list of words as input
    func = np.vectorize(lambda x: check_compatibility_word_pattern(x, word, pattern))

    # Apply func to 'guesses' and return
    return func(guesses)


def possible_words_from_pattern(word: str, pattern: list, allowed_guesses: list) -> list:
    """
    Compiles reduced phase space (version space), i.e. generates list of words which are still possible solutions after word has been guessed and pattern was given as feedback from Wordle.

    Args:
        word (str): Word that was entered into Wordle
        pattern (list): Feedback from Wordle for the guessed word encoded as five-element list containing 0, 1, 2
        allowed_guesses (list): Phase space, i.e. words which are allowed to be guessed by the player

    Returns:
        list: Collection of words which are compatible with the given pattern and word
    """

    # Generate array of bools stating whether guess from 'allowed_guesses' is compatible with word and pattern
    compatibility = vectorized_check_compatibility_word_pattern(allowed_guesses, word, pattern)

    # Obtain position where 'compatibility' is True
    positions = np.where(compatibility == True)

    # Return compatible words from 'allowed_guesses'
    return np.take(allowed_guesses, positions)[0]


    """
    # Version without Numpy

    possible_solutions = []

    # Loop through each point 'guess' from phase space
    for guess in allowed_guesses:

        if check_compatibility_word_pattern(guess, word, pattern):
            possible_solutions.append(guess)

    return np.array(possible_solutions)
    """

def expected_information(word: str, patterns: list, allowed_guesses: list) -> float:
    Omega = len(allowed_guesses)
    var = 0
    for pat in patterns:
        p = len(possible_words_from_pattern(word, pat, allowed_guesses)) / Omega
        if p == 0.0:
            continue
        else:
            var += p * np.log2(p)
    return - var




def probabilities_patterns(word):
    patterns = generate_patterns()
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


def test(pattern, word):
    count = 0

    for guess in allowed_guesses:
        for i in range(len(pattern)):
            if pattern[i] == 0 and word[i] in guess:
                break
            elif pattern[i] == 1 and (word[i] not in guess or word[i] == guess[i]):
                break
            elif pattern[i] == 2 and word[i] != guess[i]:
                break
        else:
            count += 1

    return count


# %%
if __name__ == "__main__":
    # Paths to solution words and allowed guesses
    solutions_path = "Data\wordle_answers.txt"
    guesses_path = "Data\wordle_guesses.txt"

    # Read files and create lists containing solution words and allowed guesses
    allowed_guesses, solutions = read_word_files(solutions_path, guesses_path)

    patterns = generate_patterns()

    #version_space = possible_words_from_pattern("crane", [2, 2, 0, 0, 1], allowed_guesses)
    #print(version_space)

    #pattern = [0, 0, 0, 0, 0]
    #word = "weary"
    #print(test(pattern, word))

    words = np.random.choice(allowed_guesses, 20)
    for w in words:
        e = expected_information(w, patterns, allowed_guesses)
        print(f"For '{w}': E_w = {e}")

# %%
