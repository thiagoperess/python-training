# Exercício 13

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um 
# algoritmo que calcule seu peso ideal,utilizando as seguintes fórmulas:
#
# Para homens: (72.7*h) - 58;
# Para mulheres: (62.1*h) - 44.7.

height = float(input('Qual sua altura? '))
woman, man = 'f', 'm'

gender = str(input('Qual sexo [F/M]? ')).lower()

if gender in 'f':
    print(f'Você tem {height:.2f}cm de altura. \
            O peso ideal para uma mulher de sua altura é \
            {(62.1  * height) - 44.7:.1f}Kg.')

else:
    print(f'Você tem {height:.2f}cm de altura. \
            O peso ideal para um homem de sua altura é \
            {(72.7 * height) - 58:.1f}Kg.')
                
print('Fim')