# Exercício 38

# Um funcionário de uma empresa recebe plus salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu plus de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os plus salariais sempre correspondem ao 
# dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. 
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
year = 1995
plus = 0.015

cash = float(input('Salário em 1995: '))
current_year = int(input('Ano atual: '))

while year < current_year:
    year += 1
    cash *= 1 + plus
    plus *= 2

print(f'O salário em {year}: R$ {cash:.2f}')