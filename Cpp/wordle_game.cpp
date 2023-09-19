#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include "read_csv.hpp"
#include "help_functions.hpp"

std::string get_random(std::vector<std::string> &str)
{
    srand(time(NULL));
    unsigned int random = rand() % str.size();
    std::string sel_elem = str[random];
    return sel_elem;
}

void worlde(std::vector<std::string> &allowed_guesses,
            std::vector<std::string> &allowed_answers,
            unsigned int allowed_attempts)
{
    std::string solution = get_random(allowed_answers);
    unsigned int attempt = 1;
    std::string guess = "";
    std::string str;
    while (attempt < allowed_attempts + 1)
    {
        std::cout << "Gebe deinen Guess ein: ";
        guess = "";
        std::cin >> guess;
        //guess[0] = toupper(guess[0]);
        if (!(std::binary_search(allowed_guesses.begin(), allowed_guesses.end(), guess)))
        {

            std::cout << "Invalid guess! Try again. \n";
            continue;
        }

        else if (guess == solution)
        {
            std::cout << "You have won! The word \n";
            break;
        }

        else
        {
            str = "";
            str = give_pattern(guess,solution);
            
            for (unsigned j = 0; j < str.size(); j++)
            {
            if (j != 0)
            {
                std::cout << ", ";
            }
            std::cout << str[j];
            }
            std::cout << "\n";
        }
        attempt ++;
        
    }

    std::cout << "The correct word was: " << solution << "\n";
    std::cout << "Versuche: " << attempt;
}

/* int main()
{

    std::vector<std::string> allowed_guesses = read_csv("Data/wordle_guesses.txt");
    std::vector<std::string> allowed_answers = read_csv("Data/wordle_answers.txt");

    // join both txt in vectors
    allowed_guesses.insert(allowed_guesses.end(), allowed_answers.begin(), allowed_answers.end());
    std::sort(allowed_guesses.begin(), allowed_guesses.end());

    worlde(allowed_guesses, allowed_answers, 6);
} */