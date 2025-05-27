#include <iostream>
#include <cassert>

/**************************************************************************************************************************************************/
//helper functions
double pow(double number, int exponent);
bool isDuplicate(int entry, int* array, std::size_t cap,std::size_t index);
double *geometric( double a, double ratio, std::size_t cap );
double *cross_correlation(double array0[], std::size_t cap0, double array1[], std::size_t cap1);
std::size_t shift_duplicates( int array[], std::size_t capacity );
void deallocate( double *&ptr, bool is_array, std::size_t capacity);
double pow(double number, std::size_t exponent){
    double result = 1.0;
    for (std::size_t x=0; x<exponent; x++) {
        result *= number;
    }
    return result;
}

bool isDuplicate(int entry, int* array, std::size_t cap, std::size_t index){
    for(std::size_t x=0; x<cap; x++){
        if(array[x]==entry){
            if(x==index){
                return false;
            }
            else{
                return true;
            }
        }
    }
    return false;
}
/**************************************************************************************************************************************************/

//Function 1
double *geometric( double a, double ratio, std::size_t cap ){
    double *ptr_arrayf1(new double[cap]());
    for(std::size_t x=0; x<cap; x++){
        double y = pow(ratio,x);
        ptr_arrayf1[x]=(a*y);
    }
    return ptr_arrayf1;
}

//Function 2
double *cross_correlation(double array0[], std::size_t cap0, double array1[], std::size_t cap1){
    assert(cap0+cap1 >= 1);
    double *ptr_arrayf2(new double[cap0+cap1-1]());
    if(cap0==0 || cap1==0){
        return ptr_arrayf2;
    }
    for(std::size_t i=0; i<cap0; i++){
        for(std::size_t j=0; j<cap1; j++){
            ptr_arrayf2[i+j]+=array0[i]*array1[j];
        }
    }
    return ptr_arrayf2;
}

//Function 3
std::size_t shift_duplicates( int array[], std::size_t capacity ){
    if(capacity==0){
        return 0;
    }
    int uniIndex{0};
    for(std::size_t x=1; x<capacity; x++){
        if (isDuplicate(array[x], array, capacity,x)){
            //do nothing
        }
        else{
            uniIndex++;
            std::swap(array[uniIndex],array[x]);
        }
    }
    return (uniIndex+1);
}

//Function 4
void deallocate( double *&ptr, bool is_array, std::size_t capacity = 0 ){
    if(is_array){
        for(std::size_t x{0}; x<capacity; x++){
            ptr[x]=0;
        }
        delete [] ptr;

    }
    else{
        *ptr=0;
        delete ptr;
    }
    ptr=nullptr;
}
/**************************************************************************************************************************************************/

int main() {
    return 0;
}