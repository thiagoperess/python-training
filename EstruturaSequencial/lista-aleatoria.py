# Faça um programa que peça ao usuário que ele digite oito valores.
# Ao final, o programa deverá exibir os números digitados na ordem e,
# em seguida, uma lista com os números embaralhados.

from time import sleep
from random import shuffle
numberList = []
for i in range(1, 9):
    number = int(input(f'Digite o {i}º número: '))
    numberList.append(number)
for n in range(0, 8):
    sleep(1)
    print(f'O {n+1}º número escolhido foi ', end='')
    print(numberList[n])
sleep(1)
shuffle(numberList)
print(f'Os números escolhidos foram {numberList}')
