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

lado = []
for i in range(3):
    lados = float(input(f'{i+1}º lado: '))
    lado.append(lados)

if lado[0] < lado[1] + lado[2] and \
   lado[1] < lado[2] + lado[0] and \
   lado[2] < lado[1] + lado[0]:
    print('Estas retas PODEM formar um triângulo!')

    if lado[0] == lado[1] and \
       lado[0] == lado[2] and \
       lado[1] == lado[2]:
        print('Formamos um triâgulo EQUILÁTERO.')

    elif lado[1] == lado[0] != lado[2] or \
         lado[2] == lado[1] != lado[0] or \
         lado[0] == lado[2] != lado[1]:
          print('Formamos um triângulo ISÓSCELES.')

    elif lado[0] != lado[1] and \
         lado[0] != lado[2] and \
         lado[1] != lado[2]:
          print('Formamos um triângulo ESCALENO.')
else:
    print('Estas retas NÃO PODEM formar um triângulo')