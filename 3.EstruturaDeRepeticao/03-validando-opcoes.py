# Exercício 03

# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# Solução

name = input('Nome: [minimo 4 letras]: ')
age = int(input('Sua idade: '))
salary = float(input('Salário: '))
gender = input('Sexo [F/M]: ')
status = input('Estado civil [S/C/V/D]: ')



def valid_options(name, age, salary, gender, status):

    while True:
        if len(name) <= 3: 
            name = input('No mínimo 3 letras: ')

        elif 0 > age < 150: 
            age = int(input('Idade entre 0 e 150: '))

        elif salary < 0: 
            salary = float(input('Salário negativo: '))

        elif gender not in 'mf': 
            gender = input('Sexo Inválido: ')

        elif status not in 'scvd': 
            status = input('Estado civil [S/C/V/D]: ')

        break

valid_options(name, age, salary, gender, status)
