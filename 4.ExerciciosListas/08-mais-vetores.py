# Exercício 08

# Faça um Programa que peça a idade e a altura de 5 pessoas, 
# armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.


alturas = []
idades = []

for i in range(5):
    print(f'{i+1}ª pessoa:')

    idade = int(input(f'Qual a idade? '))
    altura = float(input(f'Qual a altura? '))

    idades.append(idade)
    alturas.append(altura)



print(
      f'Alturas\n'
      f'{alturas[::-1]}\n'
      f'Idades\n'
      f'{idades[::-1]}'
     )