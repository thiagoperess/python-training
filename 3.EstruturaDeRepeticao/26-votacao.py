# Exercício 26

# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
 
qty_votes = 0

while (qty_votes <= 0):
    qty_votes = int(input('Quantidade de eleitores: '))
    
cand1, cand2, cand3 = 0, 0, 0

for i in range(0, qty_votes):
    
    vote = 0
    while vote < 1 or vote > 3:
        print(f'{i+1}º ELEITOR')
        vote = int(input('Candidato 1, 2 ou 3? '))

        if vote < 1 or vote > 3:
            print ('Candidato invalido!')
            
    if vote == 1: cand1 += 1
    elif vote == 2: cand2 += 1
    else: cand3 += 1

print (f'''

Resultado:
Candidato 1: {cand1}
Candidato 2: {cand2}
Candidato 3: {cand3}

''')
