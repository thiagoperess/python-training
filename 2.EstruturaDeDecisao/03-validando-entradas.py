# Exercício 03

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

sexo = str(input('Digite o sexo: '))
if sexo in 'Ff':
    print('Feminino')
elif sexo in 'Mm':
    print('Masculino')
else:
    print('Sexo inválido')
