# Exercício 02

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, e voltando a pedir as informações.

# Solução

name, password = '', ''

while name == password:
	name = str(input('Digite o nome: '))
	password = str(input('Digite a senha: '))

else:
	print('Seus dados foram salvos')