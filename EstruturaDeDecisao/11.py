#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("Digite seu salário: R$"))

n1 = salario

if n1 <= 280:
    reajuste = n1 + (n1 * 0.20)
    print(f"Seu salario antes do reajuste era de R${salario}")
    print("Seu aumento foi de 20%")
    print(f"Seu salario com reajuste fica R${reajuste}")
    print(f"Valor do aumento: R${n1 * 0.20}")
    
if n1 > 280 and n1 < 700 :
    reajuste = n1 + (n1 * 0.15)
    print(f"Seu salario antes do reajuste era de R${salario}")
    print("Seu aumento foi de 15%")
    print(f"Seu salario com reajuste fica R${reajuste}") 
    print(f"Valor do aumento: R${n1 * 0.15}")
      
if n1 > 700 and n1 < 1500:
    reajuste = n1 + (n1 * 0.10)
    print(f"Seu salario antes do reajuste era de R${salario}")
    print("Seu aumento foi de 10%")
    print(f"Seu salario com reajuste fica R${reajuste}") 
    print(f"Valor do aumento: R${n1 * 0.10}")
    
if n1 > 1500:
    reajuste = n1 + (n1 * 0.05)
    print(f"Seu salario antes do reajuste era de R${salario}")
    print("Seu aumento foi de 5%")
    print(f"Seu salario com reajuste fica R${reajuste}")
    print(f"Valor do aumento: R${n1 * 0.05}") 