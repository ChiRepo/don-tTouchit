#include <stdio.h>
#include <string.h>
int main(){
    char a[100];
    printf("Enter a string: ");
    scanf("%[^\n]",a);
    int length=strlen(a);
    printf("The name is: %s\nstring length: %i\n",a,length);
}
