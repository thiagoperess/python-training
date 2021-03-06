# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

weightFish = float(input('Quantos kilos de peixe você pescou? '))
if weightFish > 50:
    weightFish -= 50
    excess = weightFish
    excess *= 4.0
    print(f'Você pescou {weightFish + 50:.2f}kg e passou {weightFish:.0f}kg da cota permitida.')
    print(f'Você deve pagar R${excess:.2f} de multa pelos {excess / 4:.0f}kg excendentes.')
