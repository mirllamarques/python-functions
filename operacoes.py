def operacoes (n1, operacao, n2):
  if (operacao == "soma" or operacao == "+"):
   soma = n1 + n2
   return soma
  if (operacao == "subtração" or operacao == "-"):
   subtracao = n1 - n2
   return subtracao
  if (operacao == "multiplicação" or operacao == "*"):
   multiplicacao = n1 * n2
   return multiplicacao
  if (operacao == "divisão" or operacao == "/"):
   divisao = n1 / n2
   return divisao
  else:
    return "Coloque uma operação válida (soma, subtração, multiplicação ou divisão)!"
