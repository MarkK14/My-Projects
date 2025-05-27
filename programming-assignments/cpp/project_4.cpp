#include <iostream>
#include <algorithm>
#include "p_4_header.hpp"

//Helper functions
int max_of(int x, int y){
    if (y>x){
        return y;
    }
    return x;
}

int min_of(int x, int y){
    if (y<x){
        return y;
    }
    return x;
}

void move_to_back(const std::size_t x, char * array[], std::size_t cap){
    char * ptr_a =array[x];
    for(std::size_t y=x; y<cap; y++){
        assign(array[y],array[y+1]);
    }
    assign(array[cap-1],ptr_a);
}

//Function 1
std::size_t length( char const *a ){
    std::size_t x=0;
    while(a[x]!='\0'){
        x++;
    }
    return x;
}

//Function 2
int compare( char const *str1, char const *str2 ){
    for(std::size_t x=0;;x++){
        if(str1[x]>str2[x]){
            return 1;
        }
        else if(str1[x]<str2[x]){
            return -1;
        }
        else if(str1[x]=='\0' && str2[x]=='\0'){
            return 0;
        }
    }
}

//Function 3
void assign( char *str1, char const *str2 ){
    for(std::size_t x=0;x<length(str2);x++){
        str1[x]=str2[x];
    }
    str1[length(str2)]='\0';
}

//Function 4
unsigned int distance( char const *str1, char const *str2 ){

if(length(str1)==0 || length(str2)==0){
    return max_of(length(str1),length(str2));
}
if(str1[0]==str2[0]){
    return distance(str1+1, str2+1);
}
else if(str1[0]!=str2[0]){
    return 1+std::min(std::min(distance(str1+1, str2+1),distance(str1, str2+1)),distance(str1+1, str2));
}
return 0;
}

//Function 5
std::size_t is_sorted( char *array[], std::size_t capacity ){

    for(std::size_t x=0; x<(capacity-1); x++){
        if(compare(array[x],array[x+1])>0){
            return x+1;
        }
    }
    return capacity;
}

//Function 6
void insert( char *array[], std::size_t capacity ){

    char * ptr_a = new char[length(array[capacity-1])+1];
    assign(ptr_a, array[capacity-1]);

    std::size_t x=capacity-1;
    while(x>0 && compare(array[x-1],ptr_a)>0){
                assign(array[x],array[x-1]);
                x--;
    }
    assign(array[x],ptr_a);

    delete[] ptr_a;
    ptr_a=nullptr;
}

//Function 7
void insertion_sort( char *array[], std::size_t capacity ){
    for(std::size_t x=1; x<capacity; x++){
        
        insert(array,x+1);
    }
}

//Function 8
std::size_t remove_duplicates( char *array[], std::size_t capacity ){
    std::size_t x=1; 
    while(x<capacity){
        if(compare(array[x],array[x-1])==0){
            move_to_back(x,array,capacity);
            capacity--;
        }
        else{
            x++;
        }
    }
    return capacity;
}

//Function 9
std::size_t find( char *array[], std::size_t capacity, char const *str ){
    std::size_t closest=0;
    for(std::size_t x=0; x<capacity; x++){
        if(distance(array[x],str)==0){
            return x;
        }
        else{
            if(distance(array[x],str)<distance(array[closest],str)){
                closest=x;
            }
        }
    }
    return closest;
}

//Function 10
void free_word_array( char** word_array ){
    
    delete[] word_array[0];
    word_array[0]=nullptr;
    
    delete[] word_array;
    word_array=nullptr;
}
