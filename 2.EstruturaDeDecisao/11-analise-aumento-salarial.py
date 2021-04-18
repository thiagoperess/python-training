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
    aumento20 = salario * 20 / 100
    print(f'Com salário de R$ {salario:.2f}.')
    print('Aumentando em 20%.')
    print(f'Sendo o aumento de R$ {aumento20:.2f}.')
    print(f'Seu salário fica em R$ {salario + aumento20:.2f}.')
elif 280 < salario <= 700:
    aumento15 = salario * 15 / 100
    print(f'Com salário de R$ {salario:.2f}.')
    print('Aumentando em 15%.')
    print(f'Sendo o aumento de R$ {aumento15:.2f}.')
    print(f'Seu salário fica em R$ {salario + aumento15:.2f}.')
elif salario > 700:
    aumento10 = salario * 10 / 100
    print(f'Com salário de R$ {salario:.2f}.')
    print('Aumentando em 10%.')
    print(f'Sendo o aumento de R$ {aumento10:.2f}.')
    print(f'Seu salário fica em R$ {salario + aumento10:.2f}.')

