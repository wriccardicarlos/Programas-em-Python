from math import sqrt, pow
lados  = [float(x) for x in input().split()]

a=lados[0]; b=lados[1]; c=lados[2]

if (a>sqrt((b-c)**2) and  a<b+c) or (b>sqrt((a-c)**2) and  b<a+c) or (c>sqrt((a-b)**2) and  c<b+a):
    perimetro = a+b+c
    print('Perimetro = %.1f'%perimetro)
else:    
    area = ((a+b)*c)/2
    print('Area = %.1f'%area)