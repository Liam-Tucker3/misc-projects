#include <string>
#include <iostream>
#include <vector>

int main() {

    std::cout << "Welcome to Rock Paper Scissors!" << std::endl;
    std::cout << std::endl;

    while (true) {

        std::cout << "Please enter ROCK, PAPER, SCISSORS, or QUIT" << std::endl;
        std::string option;
        std::cin >> option;

        if (option != "ROCK" && option != "PAPER" && option != "SCISSORS" && option != "QUIT") {
            std::cout << "INVALID OPTION" << std::endl;
            std::cout << std::endl;
            continue;
        }

        if (option == "QUIT") {
            std::cout << "Thank you for playing!" << std::endl;
            break;
        }

        // Getting Computer's Choice
        std::string computerChoice;
        int val = rand() % 3;
        if (val == 0) computerChoice = "ROCK";
        if (val == 1) computerChoice = "PAPER";
        if (val == 2) computerChoice = "SCISSORS";

        std::string winnerString;
        if (computerChoice == option) winnerString = "It's a tie!";
        else if (computerChoice == "ROCK" && option == "PAPER" || computerChoice == "PAPER" && option == "SCISSORS" || computerChoice == "SCISSORS" && option == "ROCK") {
            winnerString = "You win.";
        }
        else {
            winnerString = "I win.";
        }

        std::cout << "You chose " << option << ". I chose " << computerChoice << ". " << winnerString << std::endl;
        std::cout << "Please enter anything and then press enter to continue." << std::endl;
        std::string temp;
        std::cin >> temp;
        std::cout << std::endl;
    }

    return 0;
}