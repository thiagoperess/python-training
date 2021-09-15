# Exercício 11

# Altere o programa anterior para mostrar no final a soma dos números.

# Solução

vai = int(input('Início: '))
vaf = int(input('Fim: '))

lista = []
soma = 0

for i in range(vai+1, vaf):
    print(i, end=' ')
    lista.append(i)
    soma += i

print(f'A soma é {soma}')
