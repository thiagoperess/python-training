# Exercício 11

# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa
#  que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento. 

salario = int(input('Salário: '))

if salario <= 280:
    aumento = salario * 20 / 100
    percentual = '20%'
elif 280 < salario <= 700:
    aumento = salario * 15 / 100
    percentual = '15%'
elif salario > 700:
    aumento = salario * 10 / 100
    percentual = '10%'
    
print(f'Com salário de R$ {salario:.2f}.\nAumentando em {percentual}.\nSendo o aumento de R$ {aumento:.2f}.\nSeu salário fica em R$ {salario + aumento:.2f}.')