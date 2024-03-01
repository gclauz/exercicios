#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = float(input("Digite o valor de A: "))
if a == 0:
    print("Valor inválido.")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

delta = (b * b) - ((4) * (a) * (c))
x1 = (((-1) * b) + (delta ** 0.5))/(2 * a)
x2 = (((-1) * b) - (delta ** 0.5))/(2 * a)

if delta < 0:
    print("A equação não possui valores reais.")
elif delta == 0:
    x1 = x2
    print(f"A equação possui apenas uma raiz real. Raiz = {x1}")
elif delta > 0:
    print(f"A equação possui duas raizes reais. x1 = {x1} e x2 = {x2}")
    