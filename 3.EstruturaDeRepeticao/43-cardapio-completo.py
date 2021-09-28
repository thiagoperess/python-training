# Exercício 43

# O cardápio de uma lanchonete é o seguinte:

# Especificação   Código  Preço

# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

codigo = [100, 101, 102, 103, 104, 105]
valores = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]

pedidos = ['Cachorro Quente', 
           'Bauru Simples', 
           'Bauru com Ovo', 
           'Hambúrguer', 
           'Cheeseburguer', 
           'Refrigerante']

print('''

Comece seu pedido!

Produto          Código  Preço

Cachorro Quente  100     R$ 1,20
Bauru Simples    101     R$ 1,30
Bauru com ovo    102     R$ 1,50
Hambúrguer       103     R$ 1,20
Cheeseburguer    104     R$ 1,30
Refrigerante     105     R$ 1,00

''')

option = ''
pedidos = []

while option in 's':
    pedido = int(input('Código pedido: '))
    option = str(input('Deseja mais algo? '))

    for i in range(len(codigo)):
        if pedido == codigo[i]:
            valor = valores[i]
            pedidos.append(valor)
else:
    total = sum(pedidos)

print(
      f'Total R$ {total:.2f}\n'
      f'Obrigado e volte sempre!'
      )