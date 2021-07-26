# Exercício 02

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

# Solução

while True:
	name = str(input('Digite seu nome: '))
	password = str(input('Digite sua senha: '))
	if name == password:
		print('A senha não pode ser igual ao seu nome!')
	else:
		print('Seus dados foram salvos!')
		break
