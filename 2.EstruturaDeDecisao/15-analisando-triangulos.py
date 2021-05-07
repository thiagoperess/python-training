# Exercício 15

# Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes; 


print('-=' * 14)
print('ANALISANDO TRIÂNGULOS'.center(30))
print('-=' * 14)
side1 = float(input('1º lado: '))
side2 = float(input('2º lado: '))
side3 = float(input('3º lado: '))
if side1 < side2 + side3 and \
        side2 < side3 + side1 and \
        side3 < side2 + side1:
    print('Estas retas \033[1;32mPODEM\033[m formar um triângulo!')
    if side1 == side2 and \
            side1 == side3 and \
            side2 == side3:
        print('Os lados formam um triâgulo EQUILÁTERO.')
    elif side1 == side2 and side1 != side3 or \
            side2 == side3 and side2 != side1 or \
            side3 == side1 and side3 != side2:
        print('Os lados formam um triângulo ISÓSCELES.')
    elif side1 != side2 and side1 != side3 or \
            side2 != side3 and side2 != side1 or \
            side3 != side1 and side3 != side2:
        print('Os lados formam um triângulo ESCALENO.')
else:
    print('Estas retas \033[1;31mNÃO PODEM\033[m formar um triângulo')