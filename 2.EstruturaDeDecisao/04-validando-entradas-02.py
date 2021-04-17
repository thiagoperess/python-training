# Exercício 04

# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite a letra: '))
if letra in 'AaEeIiOoUu':
    print(f'A letra {letra} é uma vogal.')
else:
    print(f'A letra {letra} é uma consoante.')