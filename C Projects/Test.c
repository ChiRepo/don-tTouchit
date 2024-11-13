#include <stdio.h>
void function(){
    int a=1;
    sample:
    printf("%i\n",a);
    a++;
    if (a<=10){                     //we can't take ">=" because it will take condition for a which is greater than 10 itself.
                                   //Instead we can take "<=" so that it can take arguement as while a is lesser or "EQUAL" to 10.
        goto sample;
    }
    else{
        NULL;
    }
}
int main(){
    function();
}