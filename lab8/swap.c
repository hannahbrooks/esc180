#include <stdio.h>

int swap(int *a, int *b);

int main(void) {
    
    swap(2, 3);
    
    return 0;
}

int swap (int *a, int *b) {
    int x;
    
    x = a;
    a = b;
    b = x;

    return 1;
}
