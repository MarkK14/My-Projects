#include <iostream>
#include <cassert>

void pattern( unsigned int n ){

    for(unsigned int x{2*n + 1}; x > 0; x -= 2){
        std::string spaces(((2*n + 1) - x)/2,' ');
        std::string asterix(x,'*');
        std::cout << spaces + asterix << std::endl;
        if (x <= 2) break;
    }
    for(unsigned int x{3}; x <= 2*n + 1; x += 2){
        std::string spaces(((2*n + 1) - x)/2,' ');
        std::string asterix(x,'*');
        std::cout << spaces + asterix << std::endl;
    }
}

unsigned int log10( unsigned int n ){
    assert(n>0);
    unsigned int m{0};
    while(n){
        n/=10;
        m++;
    }
    return m-1;
}

unsigned int count( unsigned int n, unsigned int bit ){
    assert(bit==0 || bit==1);
    unsigned int counter{0};
    for(int x{0};x<32;x++){
        
        if((n&1)==bit){
            counter++;
        }
        n=n>>1;
    }
    return counter;
}

unsigned int swap_bytes( unsigned int n, unsigned int b0, unsigned int b1 ){
    assert(b0>=0 && b0<=3 && b1>=0 && b1<=3);
    if(b0==b1){
        return n;  
    }
    int byteofb0=(n>>(b0*8)) & 0xFF;
    int byteofb1=(n>> (b1*8)) & 0xFF;
    n &= ~((0xFF << (b0 * 8)) | (0xFF << (b1 * 8)));
    n |=(byteofb0<<(b1*8))|(byteofb1<<(b0*8));
    return n;
}


int main() {
// tests for Function 1
    pattern(1);
    pattern(5);

// tests for Function 2
    // std::cout<<log10(100);
    // std::cout<<log10(1000);
    // std::cout<<log10(999);

// tests for Function 3
    // std::cout<<count(32,0)<<std::endl;

// tests for Function 4
// std::cout<<swap_bytes(a,2,3);
return 0;
}