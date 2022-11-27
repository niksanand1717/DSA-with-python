#include<stdio.h>

int* func(){
    int a = 7;
    int *ptr = &a;
    return ptr;
}

int main(){

    if(*func() == NULL)
        printf("True\n");
    // else if(*func() == 7)
        printf("%d\n", *func());
    return 0;
    
}