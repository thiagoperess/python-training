# Exercício 45

# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o 
# programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
# gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 

# Após todos os alunos terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.

# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

# Após concluir isto você poderia incrementar o programa permitindo que 
# o professor digite o gabarito da prova antes dos alunos usarem o programa.

# gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

gabarito = []

print('Olá, professor! Digite a seguir o gabarito.')

for i in range(10):
    alternativas = input(f'Alternativa {i+1}: ').upper()
    gabarito.append(alternativas)

n, opt = 0, ''
alunos = []
while True:
    opt = str(input('Deseja cadastrar? [S/N] ')).lower()
    if opt in 's':
        print(f'Aluno {n+1}:')
        print('Assinale a alternativa: [A/B/C/D/E]')
        n += 1

        nota = 0
        respostas = []
        for i in range(len(gabarito)):
            resposta = input(f'{i+1}ª Resposta: ').upper()
            respostas.append(resposta)


            if respostas[i] == gabarito[i]:
                nota += 1
    else:
        print(
              f'GABARITO DA PROVA\n'
              f'{gabarito}\n'
             )

        break
    
    alunos.append(nota)

for i in range(len(alunos)):
    print(f'{i+1}º Aluno: {alunos[i]}')

media = sum(alunos) / len(alunos)

print(
      f'{len(alunos)} alunos fizeram o exame\n'
      f'A maior nota foi {max(alunos)}\n'
      f'A menor nota foi {min(alunos)}\n'
      f'A média da turma foi {media:.2f}'
     )
