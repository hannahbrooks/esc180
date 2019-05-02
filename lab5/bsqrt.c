float bsqrt(float x, float tol);
float abs(float x);

float bsqrt(float x, float tol) {
        float sqrt_x;
        sqrt_x = sqrt_x/2;
        while (abs(x-sqrt_x*sqrt_x) > tol) {
            x_sqrt = (x_sqrt + x/sqrt_x)/2;
        }
        return x_sqrt;
}

float abs(float x) {
        if (x>0)
                return x;
        else if (x<0)
                return -x;
        else
                return 0;
}
