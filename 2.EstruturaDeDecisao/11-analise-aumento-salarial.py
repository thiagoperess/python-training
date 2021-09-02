# Exercício 11

# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contraram para desenvolver o programa que calculará os reajustes. 
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo 
# o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%.
 
# Após o aumento ser realizado, informe na tela:

# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento. 

cash = int(input('Salário: R$ '))

if cash <= 280:
    perc = 20

elif 280 < cash < 700:
    perc = 15

elif 700 <= cash <= 1500:
    perc = 10

elif cash > 1500:
    perc = 5

plus = cash * perc / 100
        
print(f'''Salário: R$ {cash:.2f}. 
          Aumento em {perc}%, 
          sendo R$ {plus:.2f}. 
          Total: R$ {cash + plus:.2f}.
          ''')

          