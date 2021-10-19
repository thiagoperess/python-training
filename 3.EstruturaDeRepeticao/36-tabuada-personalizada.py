# Exercício 36

# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado 
# pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
# o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:

# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

from time import sleep

base = int(input('Montar a tabuada de: '))
initial = int(input('Começar em: '))
final = int(input('Terminar em: '))

while initial > final:
    initial = int(input('O início deve ser menor: '))
    final = int(input('Terminar em: '))

sleep(0.7)    
print(f'Tabuada de {base} começando em {initial} e terminando em {final}: ')

sleep(1)
for c in range(initial, final+1):
    print(f'{base} X {c} = {base*c}')
    sleep(1)
