# Exercício 16

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# metros = int(input('m² a serem pintados: '))

# litros = metros / 3
# precoL, capacidadeL = 80.0, 18.0
# latas = litros / capacidadeL

# print(f'''Você usara {latas:.0f} latas de tinta
#         O preco total é: R$ {latas*80:.2f}''')

metros = float(input('m² a serem pintados: '))

litros = metros / 3.0
latas = int(litros / 18.0)
if litros % 18 != 0:
    latas += 1

print(f'''Você usara {latas:.0f} latas de tinta
        O preco total é: R$ {latas*80:.2f}''')