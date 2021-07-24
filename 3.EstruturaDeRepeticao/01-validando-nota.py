# Exercício 01

# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# Solução

number = int(input('Digite uma nota: '))

while number > 10:
    number = int(input('Nota inválida!\nFavor digitar um número de 0 à 10: '))

print(f'Você digitou {number}. Esta é uma nota válida!\nFIM!')