# Exercício 33

# O Departamento Estadual de Meteorologia lhe contratou para desenvolver 
# um programa que leia um conjunto indeterminado de temperaturas, 
# e informe ao final a menor e a maior temperaturas informadas, 
# bem como a média das temperaturas.

qtyTemp = int(input('Quantos dias: '))

tempList = []
for i in range(qtyTemp):
    temperaturas = int(input(f'Tempo no {i+1}º dia: '))
        
    tempList.append(temperaturas)

print(tempList)

mean = (sum(tempList) / qtyTemp)

print(f'Máxima de {max(tempList):.0f}°C;\
        Mínima de {min(tempList):.0f}°C;\
        Média de {mean:.0f}°C.')
