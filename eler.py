import math
eps=10**-11
ch_el=1
pred=1.5-math.log(2)
print(pred)
n=2
shag=100000
while(math.fabs(pred-ch_el)>=eps):
    ch_el=pred
    n=n+shag
    pred=ch_el+math.log(n-shag)+sum([1/(k+n+1-shag) for k in range(0,shag)])-math.log(n)
    print(pred)
ch_el=pred
print(ch_el)    
