# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

fahrenheit = int(input('Digite a temperatura em graus Fahrenheit (Fº): '))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f'A temperatura de {fahrenheit}ºF correspondem a {celsius:.0f}ºC.')
