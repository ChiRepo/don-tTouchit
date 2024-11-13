#include <stdio.h>

int main(){
    int i[]={67848,7643,34523,4323,23423,1235,98065,64575,10986};
    int search;
    printf("[");
    int arr_len=sizeof(i)/sizeof(i[0]);
    for ( int j = 0; j < arr_len; j++)
    {
        while (j<9){
            printf(" %d", i[j]);
            while (j<9){
                printf(",");
                break;
                if (j<9){
                    break;
                }
                else{
                    continue;
                }
            }
        }
    }
    printf("]\n\nLength = %i\n",arr_len);
    printf("\nEnter the desired number: ");
    scanf("%d", &search); 
    
    for ( int k = 0; k < arr_len; k++)
    {
        if (search==i[k]){
            printf("\nThe element %d is found at %dth location",search, k);
        }
        else{
            printf("\nElement not found.\n");
            break;
        }

    }
    
}