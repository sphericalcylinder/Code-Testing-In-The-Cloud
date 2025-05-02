#include <iostream>
#include <string>
#include <format>

int main() {
    std::string mystring = "lalala";

    std::cout << "Mystring is: " << mystring << "!";
    std::cout << std::format("Mystring is: {}!\n", mystring);
}