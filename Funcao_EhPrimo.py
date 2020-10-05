# -*- coding: utf-8 -*-
from math import sqrt
def EhPrimo(numero):
  x=0

  while x<numero:

    ehprimo=True
    x=x+1
    for i in range(2,int(sqrt(numero))+1):
        if numero % i ==0:
            ehprimo=False
            break
    if ehprimo:
       return("Eh Primo")
    else:
        return("Nao Eh Primo")

