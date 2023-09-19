#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include "read_csv.hpp"
#include "help_functions.hpp"
#include "wordle_game.hpp"

double worlde_simu(std::vector<std::string> & red_pp, std::vector<std::string> &allowed_guesses, std::vector<std::string> &allowed_answers,unsigned int allowed_attempts,std::string word, std::vector<std::string> &patterns)
{
    // Setup for each iteration
    
    red_pp = allowed_guesses;
    double attempt = 1.0;
    std:: string solution;
    solution = get_random(allowed_answers);
    std:: string pattern;
    std:: vector<double> exp_inf;
    int ind_max_exp_inf;
    std:: string best_word;

    
    while (attempt < allowed_attempts + 1){
        pattern = give_pattern(word,solution);

        red_pp = possible_words(word, pattern, red_pp);
        exp_inf = generate_exp_inf(red_pp,patterns,red_pp);

        ind_max_exp_inf = max_element(exp_inf.begin(),exp_inf.end()) - exp_inf.begin();
        best_word = red_pp[ind_max_exp_inf];

        if (word == solution){
            return attempt;
        }
        else {
            attempt++;
            word = best_word;
        }
    }
    return attempt;
}

void run_simu(std::vector<std::string> & red_pp,std::vector<std::string> &allowed_guesses, std::vector<std::string> &allowed_answers,unsigned iterations){
    double iter_divider = iterations + 0.0;
    double total_attempts = 0.0;
    double current_attempt;
    double avg_attempts;
    
    std::vector<std::string> patterns = generate_patterns();
    for (unsigned i = 0; i<iterations; i++){
        current_attempt = worlde_simu(red_pp,allowed_guesses,allowed_answers,6, "tares",patterns);
        total_attempts += current_attempt;
        std:: cout << i << "\n";
    }
    avg_attempts = total_attempts / iter_divider;
    std:: cout << "Iterationen: " << iterations << "\n";
    std:: cout << "Durschnittlichen Attempts: " << avg_attempts;
    
}

int main()
{
    std::vector<std::string> allowed_guesses = read_csv("Data/wordle_guesses.txt");
    
    std::vector<std::string> allowed_answers = read_csv("Data/wordle_answers.txt");

    // join both txt in vectors
    allowed_guesses.insert(allowed_guesses.end(), allowed_answers.begin(), allowed_answers.end());
    std::sort(allowed_guesses.begin(), allowed_guesses.end());

    // init variables
    std::vector<std::string> red_pp;

    run_simu(red_pp,allowed_guesses,allowed_answers,1000);
}