# Exercício 44

# Em uma eleição presidencial existem quatro candidatos. 
# Os votos são informados por meio de código. Os códigos utilizados são:

# 1, 2, 3, 4 - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco

# Faça um programa que calcule e mostre:

# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. 
 
# Para finalizar o conjunto de votos tem-se o valor zero.

while True:
    qty_votes = int(input('Quantidade de votos: '))

    if qty_votes == 0:
        break
    
    c1, c2, c3, c4, nulo, branco = 0, 0, 0, 0, 0, 0

    print('''

CANDIDATOS

Huguinho (1)
Zezinho: (2)
Luizinho: (3)
Tio Patinhas (4)
Nulo (5)
Branco (6) 

''')

    for i in range(0, qty_votes):
        vote = 0
        while vote < 1 or vote > 6:
            i += 1
            vote = int(input(f'{i}º voto: '))
                
            if vote == 1: c1 += 1
            elif vote == 2: c2 += 1
            elif vote == 3: c3 += 1
            elif vote == 4: c4 += 1
            elif vote == 5: nulo += 1
            elif vote == 6: branco += 1
            
            else: 
                print ('Candidato invalido!')

    total = c1 + c2 + c3 + c4 + nulo + branco

    print (f'''

Resultado:

Huguinho     : {c1}
Zezinho      : {c2}
Luizinho     : {c3}
Tio Patinhas : {c4}
Nulos        : {nulo}
Brancos      : {branco} 
% Nulos      : {nulo * 100 / total:.1f}%
% Brancos    : {branco * 100 / total:.1f}%

''')
