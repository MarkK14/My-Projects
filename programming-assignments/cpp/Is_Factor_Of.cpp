#include <iostream>
int main();
int main() {
int n{2346};
int y=n;
int b{0};
int c{0};
if(n>99){
    n=n%100;
}

b=(n/10)+(n%10);

c=(b+c)%4;

if(c==0){
    std::cout<<y<<" is divisible by 4";
}else{
    std::cout<<y<<" is not divisible by 4";
}

return 0;
}