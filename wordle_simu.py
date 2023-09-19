#%%
import wordle_solver
import wordle_main
import wordle_statistics
import copy
import numpy as np
import test_cy
import char_position_statistics

#%%
def give_pattern(guess,solution):

    if guess == solution:

            return [2,2,2,2,2]

    else:

        # Create array which will encode feedback for every letter in guess
        feedback = []

        for i, letter in enumerate(guess):

            # Case 1: Letter at correct position
            if letter == solution[i]:
                feedback.append(2)

            # Case 2: Letter in word but at a different position
            elif letter in solution:
                feedback.append(1)

            # Case 3: Letter not in word
            else:
                feedback.append(0)
        
        return feedback

def run_simu(iterations):
    total_attempts= 0
    for i in range(iterations):
        current_attempt = worlde_simu(6,allowed_guesses)
        total_attempts+=current_attempt
        print(i)
    avg_attempts = total_attempts/iterations
    print(f"Die durchschnittlichen Attempts über {iterations} Iterationen betrugen: {avg_attempts}") 

def worlde_simu(allowed_attempts, allowed_guesses):

    #phase_space = copy.deepcopy(allowed_guesses)
    attempt = 1
    word = 'cares'
    
    patterns = wordle_statistics.generate_patterns()
    allowed_guesses, solutions = wordle_main.read_word_files(
        solutions_path, guesses_path)
    solution = np.random.choice(solutions)
    while attempt < allowed_attempts + 1:
        pattern = give_pattern(word,solution)

        #char comparison algorithm
        """ red_pp = char_position_statistics.possible_words(word, pattern, allowed_guesses)
        exp_inf = char_position_statistics.determine_frequency_for_each_word(red_pp) """
       
        #compute solution space algortihm
        red_pp = test_cy.possible_words(word, pattern, allowed_guesses)
        exp_inf = test_cy.generate_exp_inf(red_pp,patterns,red_pp)

        ind_max_exp_inf = np.argmax(exp_inf)
        best_word = red_pp[ind_max_exp_inf]

        allowed_guesses = red_pp

        if word == solution:
            return attempt
        else:
            attempt += 1
            
            word = best_word

    return attempt


if __name__ == "__main__":
    solutions_path = "Data/wordle_answers.txt"
    guesses_path = "Data/wordle_guesses.txt"

    allowed_guesses, solutions = wordle_main.read_word_files(
        solutions_path, guesses_path)
    run_simu(1000)
    #worlde_simu(6, allowed_guesses)
    #print(give_pattern('cares','tares'))

# %%
