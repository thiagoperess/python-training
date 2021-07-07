# Exercício 20

# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

cont = 0
lst = []
for i in range(3):
    notas = int(input(f'Nota {i+1}: '))
    lst.append(notas)
    cont += 1

media = sum(lst) / cont

if media == 10:
    print(f'Aprovado com média {media} e Distinção!')

elif 7 <= media < 10:
    print(f'Aprovado com média {media}. Parabéns!')

else:
    print(f'Com média {media} você foi reprovado!')