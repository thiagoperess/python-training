# Exercício 25

# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# Solução

qty_plus = 0

status = {  2 : 'Suspeito(a)',
            3 : 'Cúmplice',
            4 : 'Cúmplice',
            5 : 'Assassino(a)'}

ls_quest = [  'Telefonou para a vítima?',
                    'Esteve no local do crime?',
                    'Mora perto da vítima?',
                    'Devia para a vítima?',
                    'Já trabalhou com a vítima?']

for i in range(len(ls_quest)):
    print(ls_quest[i] + ' [S/N]: ')

    answer = input('Resp.: ').strip()

    if answer.lower() == 's':
        qty_plus += 1

if qty_plus in status:
    print(f'{qty_plus} Afirmações. ' + status[qty_plus])
else:
    print(f'{qty_plus} Afirmações. Inocente')