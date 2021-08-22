# Exercício 28

# Faça um programa que calcule o valor total investido por um colecionador 
# em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qty_cds = int(input('CDs comprados: '))

cds = []
for i in range(qty_cds):
    price = float(input(f'Preço pago pelo {i+1}º CD: '))
    cds.append(price)

mean = (sum(cds) / qty_cds)

print(f'Total de CDs: {qty_cds}\nValor médio: R${mean:.2f}.')
