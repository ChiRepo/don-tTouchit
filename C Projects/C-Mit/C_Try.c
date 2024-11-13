#include <stdio.h>
int main(){
    printf("\tHello world!\n");
    int a;
    int b;
    printf("Enter Variable a= ");
    scanf("%i",&a);
    printf("Enter Variable b: ");
    scanf("%i",&b);
    printf("\tVariable a: %i\n\tVariable b: %i\n\tMultiplication of both variables are: %i\n\tAddition of both variables are: %i\n\tSubstraction of both variables is: %i\n\tDividing both variables: %i\n",a,b,a*b,a+b,a-b,a/b);

}
