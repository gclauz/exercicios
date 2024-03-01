ganho_hora = float(input("Quanto você ganha por hora? "))
horas = float(input("Número de horas trabalhadas no mês: "))

a = ganho_hora * horas
b = a * 0.11
c = a * 0.08
d = a * 0.05
salario_liquido = (a - b - c - d)

print("+ Salário Bruto : R$", a)
print("- IR (11%) : R$", b)
print("- INSS (8%) : R$", c)
print("- Sindicato ( 5%) : R$", d)
print("= Salário Liquido : R$", salario_liquido)