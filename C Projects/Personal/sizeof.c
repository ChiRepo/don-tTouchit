#include <stdio.h>
int a[]={10,100,1000,200,30};
int b=10;
int main(){
    int size= sizeof(a)/sizeof(a[0]);
    int sizeb=sizeof(b)/sizeof(b);
    printf("Elements of a: {");
    for (int i=0;i<=size;i++){
        printf("%i,",a[i]);
    }
    printf("}\nElements present in a: %i\n",size);
    printf("Elements of b: {%i}\nElements present in b: %i\n",b,sizeb);
}
