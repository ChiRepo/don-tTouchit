#include <stdio.h>
int a[]={100,20,30,40,50};
float b[]={1.20,20.0,00.30,02.40,12.50};
char c[]={"abcdefg"};
int main(){
    int arr_size_a=sizeof(a)/sizeof(a[0]);
    int arr_size_b=sizeof(b)/sizeof(b[0]);
    int arr_size_c=sizeof(c)/sizeof(c[0])-1;
    printf("Elemtnts present in a: %i\nElemtnts present in b: %i\nElemtnts present in c: %i\na = [",arr_size_a,arr_size_b,arr_size_c);
    for (int i=0;i<arr_size_a;i++){
        printf("%d, ",a[i]);
    }
    printf("]\nb = [");
    for (int j=0;j<arr_size_b;j++){
        printf("%f, ",b[j]);
    }
    printf("]\nc = [");
    for (int k=0;k<arr_size_c;k++){
        printf("%c, ",c[k]);
    }
    printf("]\n");
}
