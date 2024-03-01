#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Digite o dia: ")) 
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data = False

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if (dia <= 31):
        data = True
        
if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia <= 30):
        data = True
        
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    if (dia <= 29):
        data = True
elif (dia <= 28):
    data = True
  
if data:
    print(f"Data: {dia}/{mes}/{ano}") 
    print("Data válida.")
else:
    print(f"Data: {dia}/{mes}/{ano}") 
    print("Data inválida.")

