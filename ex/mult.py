# multiply via addition

def mult(a,b):
    count = 0
    sum = 0
    while count<b:
        sum=sum+a
        count=count+1
    return sum

# test code
print(mult(1,1))
print(mult(1,0))
print(mult(0,1))
print(mult(1,10))
print(mult(10,1))
print(mult(2,8))
print(mult(8,2))
##########
