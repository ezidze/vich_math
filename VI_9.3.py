import math
x = [-3, 0, 1, 5]
y = [-7, 2, 4, 7]
shag = 0.00001
mass = range(1000000)
def Lagrang(arg, k):
    global x
    chislitel = 1
    znamenatel = 1
    for i in x:
        if i != x[k]:
            chislitel *= (arg-i)
            znamenatel *= (x[k]-i)
    return chislitel/znamenatel
for i in mass:
    arg = -5 + shag*i
    polinom = y[0]*Lagrang(arg,0)+y[1]*Lagrang(arg,1)+y[2]*Lagrang(arg,2)+y[3]*Lagrang(arg,3)
    if math.fabs(polinom-1) < shag:
        break
print(arg)
print(polinom)
print("В итоге, честным методом через полином Лагранжа получаем х=", arg)
input()
