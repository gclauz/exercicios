#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
     
n = int(input("Digite o número correspondente ao dia da semana: "))

if n == 1:
    print("Domingo")
elif n == 2:
    print("Segunda")
elif n == 3:
    print("Terça-Feira")
elif n == 4:
    print("Quarta-Feira")
elif n == 5:
    print("Quinta-Feira")
elif n == 6:
    print("Sexta-Feira")
elif n == 7:
    print("Sábado")
else:
    print("Valor inválido")