# Exercício 15

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.

pay_hr = float(input('Valor por hora: '))
work_hr = int(input('Horas trabalhadas: '))

slry = work_hr * pay_hr
tax = slry * 0.05
inss = slry * 0.08
ir = slry * 0.11
disc = tax + inss + ir
net_cash = slry - disc

print(
      f'''Seu salário bruto por {work_hr} horas: R$ {slry:.0f}.
      R$ {inss:.2f} de INSS, referente a 8% do bruto.
      5% de Taxa do Sindicato: pago R$ {tax:.2f}.
      R$ {ir:.2f} de Imposto de Renda, sendo 11% do bruto.
      Descontos totais: R$ {disc:.2f}. 
      Rendimento líquido: R$ {net_cash:.2f}.
''')