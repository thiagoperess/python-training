# Exercício 028

# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                 Até 5 Kg                Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
# Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.

# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

# Solução

print('\nBem Vindo ao Mercado Tabajara')
print('-' * 30)
beef = int(input('Qual carne você quer?\n1 - Filé Duplo\n2 - Alcatra\n3 - Picanha\nOpção: '))
qty_beef = int(input('Quantos kg você deseja? '))
tabajara_card = str(input('Vai comprar com o Cartão Tabajara? [S/N] ')).lower().strip()


if beef == 1:    
    filet = 0
    beef = 'Filé Duplo'

    if qty_beef <= 5:
        filet = 4.90
    else:
        filet = 5.80
    total = filet * qty_beef
    
elif beef == 2:
    beef = 'Alcatra'
    rump = 0

    if qty_beef <= 5:
        rump = 5.90
    else:
        rump = 6.80
    total = rump * qty_beef
    
else:
    steak = 0
    beef = 'Picanha'
    
    if qty_beef <= 5:
        steak = 6.90
    else:
        steak = 7.80
    total = steak * qty_beef

discount = 0

if tabajara_card == 's':
    discount = total * 0.05 
    total = total - discount

print('-' * 30)

print(f'''MERCADO TABAJARA - CUPOM FISCAL
-------------------------
Carne: {beef};
Peso: {qty_beef} Kg;
Total sem desconto R$ {total + discount:.2f};
Usou o Cartão Tabajara? {tabajara_card};
Desconto de R$ {discount:.2f};
Total com desconto R$ {total:.2f}.''')

print('-' * 30)
print('Obrigado e volte sempre!')
print('-' * 30)
