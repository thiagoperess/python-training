# Exercício 25

# Faça um programa que peça para n pessoas a sua idade, 
# ao final o programa devera verificar se a média de idade 
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, 
# dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.


qty_person = int(input('Quantas pessoas são? '))

cont = 0
lst = []
for i in range(qty_person):
    age = int(input(f'Idade da {i+1}ª pessoa: '))
    lst.append(age)
    cont += 1

media = sum(lst) / cont

print(f'Notas obtidas: {lst}')

if 0 <= media <= 25:
    print(f'A idade média é {media:.0f} anos.\
            É uma turma jovem!')
elif 26 <= media <= 60:
    print(f'A idade média é {media:.0f} anos.\
            É uma turma adulta!')
else:
    print(f'Idade média {media:.0f} anos.\
            É uma turma idosa')
