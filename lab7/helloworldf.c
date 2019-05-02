#include <stdio.h>

float bsqrt(float sq, float accy);
float myabs(float x);

int main(void) {
	int i;
        for(i=0;i<10;i++) {
                float mysqrt;
                mysqrt=bsqrt((float)i,0.001);
                printf("The sqrt of %d is %f\n",i,mysqrt);
        }
        return 0;
}

float bsqrt(float sq, float accy) {
        float est;
        est = sq/2;
        while (myabs(sq-est*est) > accy) {
            est = (est + sq/est)/2;
        }
        return est;
}

float myabs(float x) {
        if (x>0)
                return x;
        else if (x<0)
                return -x;
        else
                return 0;
}
