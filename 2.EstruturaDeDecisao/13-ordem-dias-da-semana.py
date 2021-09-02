# Exercício 31

# Faça um programa que leia um número e exiba o dia correspondente da semana:
# (1-Domingo, 2- Segunda, etc.). Outro valor deve aparecer valor inválido.

dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado',]

dia = int(input('Digite o dia: '))

while 1 < dia > 7:
    dia = int(input('Dia inválido: '))

for i in range(1,8):
    if dia == i: 
        print(dias[i-1])