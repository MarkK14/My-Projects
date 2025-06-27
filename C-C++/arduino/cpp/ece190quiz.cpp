#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <random>

// Question structure to hold data
struct Question {
    std::string text;
    std::vector<std::string> options;
    char correctAnswer;
    bool hasImage;
};

// Function to ask a question and return the result
bool askQuestion(const Question &q, int attempt) {
    std::cout << "\n" << q.text << "\n";

    for (size_t i = 0; i < q.options.size(); ++i) {
        std::cout << static_cast<char>('A' + i) << ". " << q.options[i] << "\n";
    }

    if (q.hasImage) {
        std::cout << "\nNote: Refer to the related image in your study material.\n";
    }

    std::cout << "\nYour answer: ";
    char answer;
    std::cin >> answer;
    answer = toupper(answer);

    if (answer == q.correctAnswer) {
        std::cout << "Correct!\n";
        return true;
    } else {
        if (attempt == 1) {
            std::cout << "Incorrect. You have one more attempt.\n";
        } else {
            std::cout << "Incorrect. The correct answer was: " << q.correctAnswer << "\n";
        }
        return false;
    }
}

int main() {
    // Seed random number generator
    std::srand(static_cast<unsigned>(std::time(0)));

    // List of questions
    std::vector<Question> questions = {
        {"Q1: Microwave ovens have a safety feature such that the magnetron loses power if the door is opened. This is an example of:",
         {"Receiver control", "Redundancy", "Inclusion of a safety factor", "The KISS principle", "Source control"},
         'A', false},

        {"Q2: True or False: Halving the probability of a car skidding also halves the associated risk:",
         {"True", "False"},
         'B', false},

        {"Q3: A large crane is designed to lift loads as heavy as 25 tons. The cable is sized to support loads as heavy as 200 tons. This is an example of:",
         {"Redundancy", "Failsafe design", "Infant mortality", "Inclusion of a safety factor", "Wear and tear"},
         'D', false},

        {"Q4: What is the probability that at least one of three control computers will remain functional during a flight if the probability of one malfunctioning is 0.02%?",
         {"98.00%", "94.12%", "99.99%", "99.999996%", "99.99999992%"},
         'D', false},

        {"Q5: What is social loafing?",
         {"Exerting less effort in a group than when alone", "Competing for recognition in a group", "Conforming to group opinions", "Discussing insignificant issues", "Working harder when in a group"},
         'A', false},

        {"Q6: Refer to the PERT chart. Which tasks lie on the critical path?",
         {"Tasks 1 and 2", "Tasks 1 and 4", "Tasks 3 and 4", "Tasks 2 and 4", "Tasks 2 and 3"},
         'E', true},

        {"Q7: Consider the PERT chart. What is the effect of removing the dependency of Task 3 on Task 5?",
         {"It increases by 1 day", "It increases by 2 days", "It doesn’t change", "It decreases by 1 day", "It decreases by 2 days"},
         'D', true},

        {"Q8: Your team is working on a project involving six tasks. The project ends as soon as Task 6 is complete. What is the expected project duration?",
         {"13 hours", "10 hours", "14 hours", "7 hours", "12 hours"},
         'E', false},

        {"Q9: In project management terms, the dead time associated with waiting for paperwork or paint drying is known as:",
         {"Task duration", "Task dependency", "Float time", "Down time", "Lag"},
         'E', false},

        {"Q10: What is the purpose of an org chart in project management?",
         {"Shows hierarchical reporting relationships", "Shows design process application", "Shows budget allocation", "Shows project tasks by function", "Shows task dependencies"},
         'A', false},

        {"Q11: The pressure 40 kN/m^2 is equivalent to:",
         {"0.04 N/cm^2", "0.4 N/cm^2", "4 N/cm^2", "40 N/cm^2", "400 N/cm^2"},
         'B', false},

        {"Q12: A microbe traveling at 85 μm/s takes 20 minutes to move between two dots. How far apart are the dots?",
         {"1.7 mm", "0.10 mm", "102 mm", "6120 mm", "0.028 mm"},
         'A', false},

        {"Q13: Why is the NASA Mars Climate Orbiter so noteworthy?",
         {"Failed due to excessive measurement error", "Failed due to mixed accuracy and precision", "Failed due to incorrect calculations", "Failed due to a unit conversion mistake", "Failed due to O-ring failure"},
         'D', false},

        {"Q14: What does the principle of dimensional homogeneity state?",
         {"Quantities can be equated, added, or subtracted only if their units match", "Quantities can be added, subtracted, multiplied, or divided only if their units match", "Quantities can be equated, multiplied, or divided only if their units match", "Quantities can be equated, added, or multiplied only if their units match", "Quantities can be equated, subtracted, or divided only if their units match"},
         'B', false},

        {"Q15: What is the rule of pi?",
         {"Helps construct a WBS", "Guideline for estimating task duration", "Guideline for task division", "Formula for circle circumference", "Engineering ethics reference"},
         'B', false},

        {"Q16: What are two reasonable ways of quantifying the precision of a set of measurements?",
         {"Range and standard deviation", "Half-range and midpoint", "Midpoint and standard deviation", "Mean and midpoint", "Range and mean"},
         'A', false},

        {"Q17: An engineer designs a radar gun where measurements have a Gaussian error with standard deviation 1.7 km/h. What is the minimum number of pulses to ensure the error is <0.5 km/h?",
         {"n >= 3", "n >= 4", "n >= 11", "n >= 12", "n >= 9"},
         'D', false},

        {"Q18: An engineer tells you that the power lines near your house create an electric field of 2.3 kV/m when measured on your house rooftop. Based on the significant figures provided by the engineer, what measurement error should be inferred?",
         {"±500 V/m", "±50 V/m", "±5 V/m", "±10 V/m", "±100 V/m"},
         'B', false}
    };

    // Shuffle questions
std::random_device rd;
std::mt19937 g(rd());
std::shuffle(questions.begin(), questions.end(), g);

    int correctCount = 0;

    // Ask each question
    for (const auto &q : questions) {
        bool correct = false;
        for (int attempt = 1; attempt <= 2; ++attempt) {
            correct = askQuestion(q, attempt);
            if (correct) {
                correctCount++;
                break;
            }
        }
    }

    // Display final score
    std::cout << "\nQuiz Complete! You answered " << correctCount << " out of " << questions.size() << " questions correctly.\n";

    return 0;
}
