# Exercício 15

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.

hourlyPayment = float(input('Quanto você recebe por hora? '))
hourWorked = int(input('Quantas horas você trabalhou este mês? '))
salary = hourWorked * hourlyPayment
incomeTax = salary * 0.05
inss = salary * 0.08
unionFee = salary * 0.11
discount = incomeTax + inss + unionFee
netSalary = salary - discount
print(f'Seu salário bruto referente a {hourWorked} horas trabalhadas foi de R${salary:.0f}.')
print(f'R$ {inss:.2f} foram descontados de INSS, referente a 8% do bruto.')
print(f'Foram pagos R$ {incomeTax:.2f} referentes a 5% de taxa ao sindicato.')
print(f'Foram descontados mais R$ {unionFee:.2f} de Imposto de Renda, sendo 11% do bruto.')
print(f'Com os descontos totais de {discount:.2f}, '
      f'seus rendimento líquidos são de R$ {netSalary:.2f}.')
