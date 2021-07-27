# Exercício 03

# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# Solução

name = input('Qual seu nome [minimo 4 caracteres]: ')
age = int(input('Sua idade: '))
salary = float(input('Salário: '))
gender = input('Sexo ("f" para feminino ou "m" para masculino): ')
status = input('Estado civil ("s", "c", "v" ou "d"): ')



def valid_options(name, age, salary, gender, status):


    while len(name) <= 3:
        name = input('Nome deve ter mais que 3 letras: ')

    while 0 < age > 150:
        age = int(input('Voce deve ter entre 0 e 150 anos: '))

    while salary < 0:
        salary = float(input('Salário negativo! Deve ser maior que 0: '))

    while gender not in 'mf':
        gender = input('Sexo: "f" para feminino ou "m" para masculino: ')

    while status not in 'scvd':
        status = input('Estado civil. Marcar "s", "c", "v" ou "d": ')


valid_options(name, age, salary, gender, status)
