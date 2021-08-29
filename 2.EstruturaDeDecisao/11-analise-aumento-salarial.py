# Exercício 11

# As Organizações Tabajara resolveram dar um plus de salário aos seus colaboradores 
# e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa
#  que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : plus de 20%
# salários entre R$ 280,00 e R$ 700,00 : plus de 15%
# salários entre R$ 700,00 e R$ 1500,00 : plus de 10%
# salários de R$ 1500,00 em diante : plus de 5% Após o plus ser realizado, informe na tela:

# o salário antes do reajuste;
# o percentual de plus aplicado;
# o valor do plus;
# o novo salário, após o plus. 

salary = int(input('Salário: '))

if salary <= 280:
    perc = 20
    plus = salary * perc / 100 

elif 280 < salary <= 700:
    perc = 10
    plus = salary * perc / 100

elif salary > 700:
    perc = 10
    plus = salary * perc / 100
        
print(f'''
          Salário: R$ {salary:.2f}.
          Aumento em %: {perc}.
          Aumento em R$ {plus:.2f}.
          Salário Total: R$ {salary + plus:.2f}.
          ''')