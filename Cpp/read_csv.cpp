#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

std::vector<std::string> read_csv(std::string path)
{
    std::ifstream data(path);
    std::vector<std::string> v;
    std::string line;
    while (std::getline(data, line))
    {
        std::stringstream lineStream(line);
        std::string cell;
        while (std::getline(lineStream, cell))
        {
            v.push_back(cell);
        }
    }
    return v;
}

