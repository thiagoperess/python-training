# Exercício 17

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 
# 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# Comprar apenas latas de 18 litros;
# Comprar apenas galões de 3,6 litros;
# Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga 
# e sempre arredonde os valores para cima, isto é, considere latas cheias.

size = float(input('m² a serem pintados: '))

liters = (size / 6.0) * 1.1  # 10% de folga
cans = int(liters / 18.0)
gallons = int(liters / 3.6)

# Cáculo de latas
if (liters % 18 != 0):
    cans += 1

# Cálculo de galões
if (liters % 3.6 != 0):
    gallons += 1

# Cálculo mistura latas e galões
mixCans = int(liters / 18.0)
mixGalloons = int((liters - (mixCans * 18.0)) / 3.6)
if ((liters - (mixCans * 18.0) % 3.6 != 0)):
    mixGalloons += 1

print(
    f'''Latas: {cans}. Valor: R$ {cans * 80:.2f}
    Galões: {gallons}. Valor: R$ {gallons * 25:.2f}
    Mistura: {mixCans} latas e {mixGalloons} galões. \
    Valor: R$ {(mixCans * 80 + mixGalloons * 25):.2f}
    ''')

    