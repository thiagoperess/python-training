# Exercício 40

# Foi feita uma estatística em cinco cidades brasileiras para coletar dados 
# sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# 
# a) Código da cidade;
# b) Número de veículos de passeio (em 1999);
# c) Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e) Qual a média de veículos nas cinco cidades juntas;
# f) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.



max_i = 0
max_i_cod = 0 
min_i_cod = 0
min_i = 10000000000
total_car = 0
city_under2000 = 0 
acci_city_under2000 = 0

for i in range(3):
    cod = int(input(f'\nCódigo da {i+1}ª cidade: '))
    cars = int(input('\nQuantidade de veículos: '))
    accidents = int(input('\nNúmero de acidentes: '))

    if accidents > max_i:
        max_i = accidents
        max_i_cod = cod
    elif accidents < min_i:
        min_i = accidents
        min_i_cod = cod
    
    total_car += cars

    if cars < 2000:
        city_under2000 += 1
        acci_city_under2000 += accidents
        
print(f'\nCidade com maior índice: {max_i_cod}. Total de acidentes: {max_i}'
      f'\nCidade com menor índice: {min_i_cod}. Total de acidentes: {min_i}'
      f'\nMédia de veículos: {total_car / 3:.1f}'
      f'\nMédia de acidentes cidades -2000 veículos: {acci_city_under2000 / city_under2000:.2f}')