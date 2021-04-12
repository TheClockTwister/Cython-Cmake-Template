//
// Created by User on 12/04/2021.
//

#include "../include/foobar.h"

void print_my_stuff(char* text) {
    std::string val = text;
    std::cout << val << std::endl;
}

void test_list(const std::vector<float>& liste) {
    for (auto i : liste) {
        std::cout << i << std::endl;
    }
}