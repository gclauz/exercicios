#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2)/2
conceito = ""
aprov_reprov = ""

if media >= 9 and media <= 10:
    conceito = "A"
    aprov_reprov = "APROVADO"
elif media >= 7.5 and media < 9:
    conceito = "B"
    aprov_reprov = "APROVADO"
elif media >= 6 and media < 7.5:
    conceito = "C"
    aprov_reprov = "APROVADO"
elif media >= 4 and media < 6:
    conceito = "D"
    aprov_reprov = "REPROVADO"
elif media >= 0 and media < 4 :
    conceito = "E" 
    prov_reprov = "REPROVADO"
     
print(f"\nPrimeira nota: {n1}"
      f"\nSegunda nota: {n2}"
      f"\nMédia: {media}"
      f"\nConceito correspondente a média: {conceito}"
      f"\n{aprov_reprov}")