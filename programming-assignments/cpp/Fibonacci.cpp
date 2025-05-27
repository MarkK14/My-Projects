#include <iostream>
int main();
int main() {

int a{0};
int b{1};
int k{1};
int n{20};

std::cout<<k<<"\n";
do{
k=a+b;
std::cout<<k<<"\n";
a=b;
b=k;
}while(k<n);

return 0;
}