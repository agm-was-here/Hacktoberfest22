#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
int circle(int r){
    p=2*3.14*r;
    printf ("perimeter is %d",p);
    a=3.14*r*r;
    printf ("area is %d",a);
}
int square(int a){
    area=a*a;
    p=4*a;
    printf ("perimeter is %d",p);
    printf ("area is %d",area);
}
int main ()
{
    circle(10);
    fork();
    square(5);
}