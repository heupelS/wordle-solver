#include <string>
#include <string.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <iostream>

bool check_letters(std::string &v, char word)
{
    for (unsigned i = 0; i < v.size(); i++)
    {
        if (word == v[i])
            return true;
    }
    return false;
}

std::vector<std::string> generate_patterns()
{
    std::vector<std::string> v = {};
    std::string str = "";
    for (int i = 0; i < 3; i++)
    {
        for (int k = 0; k < 3; k++)
        {
            for (int m = 0; m < 3; m++)
            {
                for (int j = 0; j < 3; j++)
                {
                    for (int h = 0; h < 3; h++)
                    {
                        str = std::to_string(i) + std::to_string(k) + std::to_string(m) + std::to_string(j) + std::to_string(h);
                        v.push_back(str);
                    }
                }
            }
        }
    }
    return v;
}

std::string give_pattern(std::string guess, std::string solution)
{
    std::string str = "";
    for (unsigned i = 0; i < 5; i++)
    {
        if (guess[i] == solution[i])
        {
            str += '2';
            continue;
        }
        else if (check_letters(solution, guess[i]))
        {
            str += '1';
            continue;
        }
        else
        {
            str += '0';
            continue;
        }
    }
    return str;
}

std::vector<std::string> possible_words(std::string word, std::string pattern, std::vector<std::string> possible_guesses)
{
    /* char wj;
    char gj; */
    std::vector<std::string> possible_solutions = {};

    for (unsigned i = 0; i < possible_guesses.size(); i++)
    {
        for (unsigned j = 0; j < pattern.size(); j++)
        {

            // wj = word[j];
            // gj = possible_guesses[i][j];

            if (check_letters(possible_guesses[i],word[j]) && pattern[j] == '0')
            {
                break;
            }

            else if (!(check_letters(possible_guesses[i],word[j]) || word[j] == possible_guesses[i][j]) && pattern[j] == '1')
            {
                break;
            }

            else if ((word[j] != possible_guesses[i][j]) && pattern[j] == '2')
            {
                break;
            }

            else if (j == 4)
            {
                possible_solutions.push_back(possible_guesses[i]);
                break;
            }
            else{continue;}
        }
    }
    return possible_solutions;
}

double exp_inf(std::string word, std::vector<std::string> patterns, std::vector<std::string> allowed_guesses)
{
    double omega = allowed_guesses.size();
    double var = 0.0;
    double p;
    
    for (unsigned i = 0; i < patterns.size(); i++)
    {
        p = (possible_words(word, patterns[i], allowed_guesses).size()) / omega;
        if (p == 0.0)
        {
            continue;
        }
        else
        {
            var += p * log2(p);
        }
    }
    return (-1)*var;
}

std::vector<double> generate_exp_inf(std::vector<std::string> words, std::vector<std::string> patterns, std::vector<std::string> allowed_guesses)
{
    std::vector<double> results = {};
    double val;
    for (unsigned i = 0; i < words.size(); i++)
    {
        val = exp_inf(words[i], patterns, allowed_guesses);
        results.push_back(val);
    }
    return results;
}

void print(std::vector<std::string> str){
    for (unsigned i= 0; i<str.size();i++){
        std::cout << str[i] << "\n";
    }
}

void print(std::string str){
    for (unsigned i= 0; i<str.size();i++){
        std::cout << str[i] << "\n";
    }
}