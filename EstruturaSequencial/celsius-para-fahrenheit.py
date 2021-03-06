# Faça um Programa que peça a temperatura em graus Celsius,
# e transforme e mostre em graus Fahrenheit:

celsius = int(input('Digite a temperatura em Celsius (Cº): '))
fahrenheit = (celsius * 9 / 5) + 32
print(f'{celsius}ºC correspondem a {fahrenheit:.0f}ºF.')
