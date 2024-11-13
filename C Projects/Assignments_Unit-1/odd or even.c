#include <stdio.h>
int main(){
    int a;
    printf("Enter a number: ");
    scanf("%i",&a);
    printf("\t\t...Analyzing is the given number is odd or even...\t\n\t");
    if (a%2!=1){
        printf("The number is even.\n");
    }
    else {
        printf("The number is odd.\n");
    }
}
