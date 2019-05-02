def gcd(a,b):
    if a == b:
        return a
    elif a > b:
        x = a
        a = b
        b = x
    while True:
        i = 0
        temp = 0
        while (temp + a) <= b:
            temp+=a
            i+=1
        remainder = b - i*a
        if remainder == 0:
            return a
            break
        else:
            b = a
            a = remainder

