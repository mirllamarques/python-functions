# Função que recebe os termos de uma equação do 2º grau e retorna um array contendo sua(s) raíz(es).

# Obs1: Caso não tenha raízes (delta < 0) , a função retornará um array vazio.
# Obs2: Caso o termo 'a' receba 0, a função mostrará um erro e retornará None.

def bhaskara(a, b=0, c=0):
  listaDeRaizes = []
  delta = (b ** 2) - (4 * a * c)

  try:
    if delta == 0:
      raiz = -b / (2 * a)
      listaDeRaizes.append(raiz)

    elif delta > 0:
      raiz1 = (-b + (delta ** 0.5)) / (2 * a)
      raiz2 = (-b - (delta ** 0.5)) / (2 * a)
      listaDeRaizes.append(raiz1)
      listaDeRaizes.append(raiz2)

    return listaDeRaizes
  
  except ZeroDivisionError:
    print("Erro: termo 'a' não pode ser 0")
    return None
