def mostrarData():
  import datetime

  data = datetime.datetime.now()
  dia = data.day
  mes = data.month
  ano = data.year

  if mes < 10:
    print(f'{dia}/0{mes}/{ano}')

  else:
    print(f'{dia}/{mes}/{ano}')
