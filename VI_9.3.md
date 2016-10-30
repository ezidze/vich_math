

```python
import math
import numpy as np
```

# Посчитаем с помощью библиотеки


```python
x = [-3, 0, 1, 5]
y = [-7, 2, 4, 7]
shag = 0.00001
mass = range(1000000)
```


```python
p2 = np.polyfit(x, y, 3)
yp = 0
```


```python
for i in mass:
    arg = -5 + shag*i
    yp = np.polyval(p2, arg)
    if math.fabs(yp-1)<shag:
        break
print(arg)
print(yp)
```

    -0.4244299999999992
    0.999997293775
    


```python
print("В итоге, x=", arg)
```

    В итоге, x= -0.4244299999999992
    

# Нахождение коэффициентов честно
## Через интерпаляционный многочлен Лагранжа  


```python
def Lagrang(arg, k):
    global x
    chislitel = 1
    znamenatel = 1
    for i in x:
        if i != x[k]:
            chislitel *= (arg-i)
            znamenatel *= (x[k]-i)
    return chislitel/znamenatel
        
```


```python
for i in mass:
    arg = -5 + shag*i
    polinom = y[0]*Lagrang(arg,0)+y[1]*Lagrang(arg,1)+y[2]*Lagrang(arg,2)+y[3]*Lagrang(arg,3)
    if math.fabs(polinom-1) < shag:
        break
print(arg)
print(polinom)
```

    -0.4244299999999992
    0.9999972937750026
    


```python
print("В итоге, честным методом через полином Лагранжа получаем х=", arg)
```

    В итоге, честным методом через полином Лагранжа получаем х= -0.4244299999999992
    


```python

```
