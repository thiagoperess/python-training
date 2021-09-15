# Exercício 028

# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                 Até 5 Kg                Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
# OBS: Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.


# Solução

print('Bem Vindo ao Mercado Tabajara')

beef = int(input('''Qual carne você quer?

1 - Filé Duplo
2 - Alcatra
3 - Picanha

Opção: '''))

qty_beef = int(input('Quantos kg você deseja? '))
card = str(input('Usa o Cartão? [S/N] ')).lower().strip()


if beef == 1:    
    beef = 'Filé Duplo'
    filet = 4.90 if qty_beef <= 5 else 5.80
    total = filet * qty_beef
    
elif beef == 2:
    beef = 'Alcatra'
    rump = 5.90 if qty_beef <= 5 else 6.80
    total = rump * qty_beef
    
elif beef == 3:
    beef = 'Picanha'
    steak = 6.90 if qty_beef <= 5 else 7.80
    total = steak * qty_beef

discount = 0

if card == 's':
    discount = total * 0.05 
    total = total - discount

print(f'''MERCADO TABAJARA - CUPOM FISCAL

Carne: {beef}
Peso: {qty_beef}Kg
Total sem desconto R${total + discount:.2f}
Usou o Cartão Tabajara? {card}
Desconto de R${discount:.2f}
Total com desconto R${total:.2f}''')

print('Obrigado e volte sempre!')
