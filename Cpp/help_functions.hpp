#include <string>
#include <vector>

bool check_letters(std::string & v, char word);

std::vector<std::string> generate_patterns();

std::string give_pattern(std::string guess, std::string solution);

std::vector<std::string> possible_words(std::string word, std::string pattern, std::vector<std::string> possible_guesses);

double exp_inf(std::string word, std::vector<std::string> patterns, std::vector<std::string> allowed_guesses);

std::vector<double> generate_exp_inf(std::vector<std::string> words, std::vector<std::string> patterns, std::vector<std::string> allowed_guesses);

void print(std::vector<std::string> str);

void print(std::string str);