#include <iostream>
#include <cmath>
int main();

double max(double a, double b){
    double max{a};
    if(a<b){
        max=b;
    }
    return max;
}

int main() {
std::cout<<"ECE 150 calculator!\tby: Mark Khairallah {21120249}\tDate: 9/16/2024"<<std::endl;
double max_grade;
double grade;
double project_grade;
double final_exam_grade;
double midterm_grade;
double exam_average;
double total_average;
double grade_sum{0};


std::cout<<"Enter Maximum Grade of the final Exam: "<<std::endl;
std::cin>>max_grade;

while(max_grade<=0 || max_grade!=std::round(max_grade)){
    std::cout<<"Maximum grade must be a positive integer! Re-Enter: "<<std::endl;
    std::cin>>max_grade;
}


std::cout<<"Enter your mark on the final Exam: "<<std::endl;
std::cin>>grade;
while(grade>max_grade || grade<=0){
    std::cout<<"your grade must be a positive integer that is less than or equal to "<<max_grade<<"! Re-Enter: "<<std::endl;
    std::cin>>grade;
}

final_exam_grade=(grade/max_grade)*100;

std::cout<<"Enter Maximum Grade of the Midterm: "<<std::endl;
std::cin>>max_grade;

while(max_grade<=0 || max_grade!=std::round(max_grade)){
    std::cout<<"Midterm grade must be a positive integer! Re-Enter: "<<std::endl;
    std::cin>>max_grade;
}

std::cout<<"Enter your mark on the Midterm: "<<std::endl;
std::cin>>grade;
while(grade>max_grade || grade<0){
    std::cout<<"your grade must be a positive integer that is less than or equal to "<<max_grade<<"! Re-Enter: "<<std::endl;
    std::cin>>grade;
}
midterm_grade=(grade/max_grade)*100.0;

midterm_grade=max(midterm_grade,final_exam_grade);

exam_average=0.75*(final_exam_grade)+0.25*(midterm_grade);
// std::cout<<exam_average<<std::endl;


if (40<exam_average && exam_average<60){

    for(int x{0};x<5;++x){
        std::cout<<"Enter Maximum Grade in project #"<<x+1<<": "<<std::endl;
        std::cin>>max_grade;
        while(max_grade<=0 || max_grade!=std::round(max_grade)){
            std::cout<<"Maximum grade must be a positive integer! Re-Enter: "<<std::endl;
            std::cin>>max_grade;
        }
        std::cout<<"Enter your mark for project #"<<x+1<<": "<<std::endl;
        std::cin>>grade;
        while(grade>max_grade || grade<0){
            std::cout<<"your grade must be a positive integer that is less than or equal to "<<max_grade<<"! Re-Enter: "<<std::endl;
            std::cin>>grade;
            
        }
        grade_sum+=max(final_exam_grade,(grade/max_grade)*100.0);
    }
    project_grade=(grade_sum)/5.0;
    // std::cout<<project_grade<<std::endl;
    total_average = project_grade*((exam_average - 40.0)/60.0) + exam_average*(1.0 - (exam_average - 40.0)/60.0);

}else if(exam_average>=60){

    for(int x{0};x<5;++x){
        std::cout<<"Enter Maximum Grade in project #"<<x+1<<": "<<std::endl;
        std::cin>>max_grade;
        while(max_grade<=0 || max_grade!=std::round(max_grade)){
        std::cout<<"Maximum grade must be a positive integer! Re-Enter: "<<std::endl;
        std::cin>>max_grade;
    }
        std::cout<<"Enter your mark for project #"<<x+1<<": "<<std::endl;
        std::cin>>grade;
        while(grade>max_grade || grade<0){
        std::cout<<"your grade must be a positive integer that is less than or equal to "<<max_grade<<"! Re-Enter: "<<std::endl;
        std::cin>>grade;
    }
        grade_sum+=max(final_exam_grade,(grade/max_grade)*100);
    }
    project_grade=(grade_sum)/5;
    // std::cout<<project_grade<<std::endl;

    total_average=(1.0/3.0)*(project_grade)+(2.0/3.0)*(exam_average);

}else{
for(int x{0};x<5;++x){
        std::cout<<"Enter Maximum Grade in project #"<<x+1<<": "<<std::endl;
        std::cin>>max_grade;
        while(max_grade<=0 || max_grade!=std::round(max_grade)){
        std::cout<<"Maximum grade must be a positive integer! Re-Enter: "<<std::endl;
        std::cin>>max_grade;
    }
        std::cout<<"Enter your mark for project #"<<x+1<<": "<<std::endl;
        std::cin>>grade;
        while(grade>max_grade || grade<0){
        std::cout<<"your grade must be a positive integer that is less than or equal to "<<max_grade<<"! Re-Enter: "<<std::endl;
        std::cin>>grade;
    }
        grade_sum+=max(final_exam_grade,(grade/max_grade)*100);
    }
    total_average=exam_average;
}


total_average = std::round( total_average + 1e-12 );
std::cout<<"Final grade: ";
std::cout<<total_average<<std::endl;

    
return 0;
}