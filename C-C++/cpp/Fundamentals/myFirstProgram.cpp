#include <iostream>
int main();
int main() {

std:: string name;
int age;
int myAge{18};

std::cout << "Hello ECE 150!"<< std::endl;
std::cout<<"My name is Mark, What's your name?"<< std::endl;
std::cin>>name;
std::cout<<"Hi there, "<<name<<" Pleasure to meet you!"<<std::endl;
std::cout<<"How old are you, "<<name<<"?"<<std::endl;
std::cin>>age;

int ageDiff{abs(myAge-age)};

if(age<myAge){
    std::cout<<"Wow you are young! I am "<<ageDiff<<" years older"<<std::endl;
}
else if(age>myAge){
    std::cout<<"Wow you are old! I am "<<ageDiff<<" years younger"<<std::endl;
}
else{
    std::cout<<"Wow I am also "<<age<<std::endl;
}
return 0;
}