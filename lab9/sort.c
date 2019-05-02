#include <stdio.h>
#include <stdbool.h>

int bubbleSort(int *array, int size);

int main(void){
   int i = 0;
   int arr[10] = {12, 3, 9, 4, 1, 5, 7, 12, 8, 15};

   printf("Original array values\n\n");
   for(i=0; i<10; i++){
      printf("%d\n", arr[i]);
   }

   bubbleSort(arr, 10);
   int j = 0;

   printf("\n\nSorted array values\n\n");
   for(j=0; j<10; j++){
      printf("%d\n", arr[j]);
   }

}

int bubbleSort(int *myarray, int size){
    int temp;
    bool swapped = true;
    int i = 0;

    for (i = 1; i < size; i++) {
        if (&myarray[i] == NULL) {
            return -1;
        }
    }

    while (swapped == true) {
        swapped = false;
        for (i = 1; i < size; i++) {
            if (myarray[i-1] > myarray[i]) {
                temp = myarray[i-1];
                myarray[i-1] = myarray[i];
                myarray[i] = temp;
                swapped = true;
            }
        }
    }
    return 0;
}
