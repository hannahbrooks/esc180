def reducingProduct(a,b):
  return a*b

def reduce(func, l):
  tot=l[0]
  for i in l[1:]:
    tot=func(i,tot)
  return tot

def fibo(n):
    if (n==0) or (n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def fiboL(n):
  L=[]
  for i in range(0,n,1):
    L+=[fibo(i)]
  return L

def redfibo(n):
  return(reduce(reducingProduct,fiboL(n)))



