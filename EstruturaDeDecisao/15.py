#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

a = float(input("Digite o valor de um dos lados do triângulo: ")) 
b = float(input("Digite o valor de outro lado do triângulo: "))
c = float(input("Digite o valor do último lado do triângulo: "))
    
if (a + b < c) or (a + c < b) or (b + c < a):
    print("Com os valores inseridos não é possível formar um triângulo")
elif (a == b) and (a ==c):
    print("Triângulo equilátero")
elif (a == b) or (a == c) or (b == c):
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")
