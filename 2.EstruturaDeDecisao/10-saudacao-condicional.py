# Exercício 10

# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
# ou "Valor Inválido!", conforme o caso. 

turno = str(input('Turno de estudo? ')).upper()

while turno not in 'MVN':
    turno = str(input('Opção Inválida: ')).upper()

if turno in 'M': print('Bom Dia')
elif turno in 'V': print('Boa Tarde')
elif turno in 'N': print('Boa noite')
    