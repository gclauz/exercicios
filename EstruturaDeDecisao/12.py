#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% 

valor_hora = float(input("Valor por hora trabalhada: "))
horas_trabalhadas = float(input("Horas trabalhadas no mês: "))

salario_bruto = (valor_hora * horas_trabalhadas)

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500 and salario_bruto > 900:
    ir = 5
elif salario_bruto <=2500 and salario_bruto > 1500:
    ir = 10
elif salario_bruto > 2500:
    ir = 20
    
ir_valor = (salario_bruto * (ir / 100))
sindicato = (salario_bruto * 0.03)
fgts = (salario_bruto * 0.11)
descontos = (ir_valor + sindicato)

    
print(f"\nSalário Bruto: ({valor_hora} * {horas_trabalhadas}): R${salario_bruto}"
      f"\n(-) IR({ir}%): R${ir_valor}"
      f"\n(-) Sindicato(3%): R${sindicato}"
      f"\nFGTS(11%): R${fgts}"
      f"\nTotal de descontos: R${descontos}"
      f"\nSalário Liquido: R${salario_bruto - descontos}")