#include <iostream>
#include <cmath>

int main(){
    std::cout<<"MK Quadratic Formula Calculator!\n";
    std::cout<<"-b +/- _/((b)^2 -4ac)\n";
    std::cout<<"_____________________\n";
    std::cout<<"         2a      \n";
    std::cout<<"\n\n ax^2 + bx +c\n";
    double a;
    double b;
    double c;
    double rad;
    double root1;
    double root2;
    std::cout<<"Enter value for a: "<<std::endl;
    std::cin>>a;
if(a==0){
    std::cout<<"variable a cannot equal 0 !!!";
}
    std::cout<<"Enter value for b: "<<std::endl;
    std::cin>>b;
    std::cout<<"Enter value for c: "<<std::endl;
    std::cin>>c;

    b*=-1;
    rad=(b*b) - 4*a*c;
    if (rad==0){
        root1=b/(2*a);
        std::cout<<"Only one root and its at x="<<root1<<std::endl;
    }else if(rad<0){
        std::cout<<"No Roots f(x) != 0"<<std::endl;
    }else{
    root1=(b + sqrt(rad))/(2*a);
    root2=(b - sqrt(rad))/(2*a);
    std::cout<<"Roots are at x="<<root1<<" and x="<<root2<<std::endl;
}
return 0;
}