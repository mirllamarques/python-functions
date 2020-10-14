def raiz(base, expoente, precisao=None):
  raiz = base ** (1 / expoente)

  if precisao != None:
    raiz = round(raiz, precisao)
  
  return raiz
