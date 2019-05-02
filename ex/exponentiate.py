def exponentiate(a,b):
    count = 0
    product = 1
    if b==0:
        product = 1
    else:
        while count<b:
            product = product * a
            count = count + 1
    return product

