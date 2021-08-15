# Exercício 14

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.

# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

wt_fish = float(input('Kg pescados: '))

if wt_fish > 50:
    wt_fish -= 50
    xs = wt_fish
    xs *= 4.0

    print(f'{wt_fish + 50:.2f}kg passam {wt_fish:.0f}kg da cota.\
          R${xs:.2f} de multa pelos {xs / 4:.0f}kg excendentes.')
else:
    print(f'{wt_fish} não passam da cota. Cobrança sem multa!')
