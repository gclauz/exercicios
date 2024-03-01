#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

#Ano bissexto = multiplo de 4 e 400, mas não de 100. 


ano = int(input("Digite o ano: "))

if (ano % 4 == 0) and (ano % 100 != 0):
    print("O ano é bissexto.")
elif (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
    