# Exercício 26

# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
 
qtyVoters = 0

while (qtyVoters <= 0):
    qtyVoters = int(input('Quantidade de votos: '))
    
Cand1, Cand2, Cand3 = 0, 0, 0

for i in range(0, qtyVoters):
    
    vote = 0
    while vote < 1 or vote > 3:
        vote = int(input('Candidato 1, 2 ou 3? '))
        if vote < 1 or vote > 3:
            print ('Candidato invalido!')
            
    if vote == 1: Cand1 += 1
    elif vote == 2: Cand2 += 1
    else: Cand3 += 1

print (f'''Resultado:
Candidato 1: {Cand1}
Candidato 2: {Cand2}
Candidato 3: {Cand3}
''')
