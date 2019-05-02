def bsqrt(sqr, acc):
    est = sqr/2
    while abs(sqr,est) > acc:
        est = (est + sqr/est)/2
        print(est)
    return est

def abs(sqr1, est1):
	if est1*est1-sqr1 < 0:
		x = -1*(est1*est1-sqr1)
	else:
		x = est1*est1-sqr1
	return x

print(bsqrt(0, 0.000000001))
