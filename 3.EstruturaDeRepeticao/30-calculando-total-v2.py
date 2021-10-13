# Exercício 30

# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
# que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela 
# de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

# Caso o cliente comprar mais de 10 pães e menos de 30, terá um desconto de 5% do valor.
# Se a compra for acima de de 30 pães, o desconte sobe para 10% do valor.  

# Preço do pão: R$ 0.50
# Panificadora Pão de Ontem - Tabela de preços

# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

qtyBreads = int(input('Quantidade de pães: '))

while qtyBreads > 50:
    qtyBreads = int(input('Só até 50 pães: '))

for i in range(qtyBreads):
    subtotal = (i+1) * 0.50

    if 10 < qtyBreads < 30:
        desconto = subtotal * 0.05
        total = subtotal - desconto

    elif qtyBreads > 30:
        desconto = subtotal * 0.10
        total = subtotal - desconto

    else:
        total = subtotal

    print(f'{i+1 } - R$ {total:.2f}')
