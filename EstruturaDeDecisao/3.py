#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

s = input("Digite M para masculino ou F para feminino: ")

if s == "M" or s == "m":
    print("Masculino")
elif s == "F" or s == "f":
    print("Feminino")
else:
    print("Sexo Inválido")