from math import sqrt

n=int(input())

x=0

while x<n:

    ehprimo=True
    num=int(input())
    x=x+1
    
    for i in range(2,int(sqrt(num))+1):
        if num % i ==0:
            ehprimo=False
            break
    if ehprimo:
        print("Eh Primo")
    else:
        print("Nao eh Primo")
