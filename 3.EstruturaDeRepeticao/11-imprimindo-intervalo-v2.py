# Exercício 11

# Altere o programa anterior para mostrar no final a soma dos números. No caso do início do intervalo ser menor que o final, o usuário deverá ser informado e solicitado a a digitar novamente.

# Solução

vai = int(input('Início: '))
vaf = int(input('Final: '))

while vai > vaf:
    print('O início maior que o final!')
    vai = int(input('Início: '))
    vaf = int(input('Fim: '))

lista = []
soma = 0

for i in range(vai+1, vaf):
    lista.append(i)
    soma += i

print(f'Lista: {lista}\n'
        f'Soma total: {soma}')
