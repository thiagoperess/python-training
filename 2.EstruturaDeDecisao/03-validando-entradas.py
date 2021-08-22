# Exercício 03

# Faça um programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

sexo = str(input('Sexo: ')).lower()

if sexo in 'f': print('Feminino')
elif sexo in 'm': print('Masculino')
else: print('Sexo inválido')
