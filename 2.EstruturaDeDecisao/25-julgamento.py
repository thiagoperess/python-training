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

count = 0

resp = str(input(
    'Telefonou para a vítima? [S/N] ')
    ).upper()
if resp == 'S':
    count += 1

resp = str(input(
    'Esteve no local do crime? [S/N] ')
    ).upper()
if resp == 'S':
    count += 1

resp = str(input(
    'Mora perto da vítima? [S/N] ')
    ).upper()
if resp == 'S':
    count += 1

resp = str(input(
    'Devia para a vítima? [S/N] ')
    ).upper()
if resp == 'S':
    count += 1

resp = str(input(
    'Já trabalhou com a vítima? [S/N] ')
    ).upper()
if resp == 'S':
    count += 1
    
if count == 2:
    print(f'{count} Afirmações Positivas. \
                    \nQualificação: Suspeito(a)')

elif count == 3 or count == 4:
    print(f'{count} Afirmações Positivas. \
                    \nQualificação: Cúmplice')

elif count == 5:
    print(f'{count} Afirmações Positivas. \
                    \nQualificação: Assassino(a)')

elif count == 0 or count < 2:
    print(f'{count} Afirmações Positivas. \
                    \nQualificação: Inocente')