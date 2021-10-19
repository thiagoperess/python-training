# Exercício 33

# O Departamento Estadual de Meteorologia lhe contratou para desenvolver 
# um programa que leia um conjunto indeterminado de temperaturas, 
# e informe ao final a menor e a maior temperaturas informadas, 
# bem como a média das temperaturas.

qty_temp = int(input('Quantos dias: '))

temp_list = []
for i in range(qty_temp):
    temperaturas = int(input(f'Tempo no {i+1}º dia: '))
        
    temp_list.append(temperaturas)

print(temp_list)

media = (sum(temp_list) / qty_temp)

print(f'Máxima de {max(temp_list):.0f}°C'
      f'Mínima de {min(temp_list):.0f}°C'
      f'Média de {media:.0f}°C.')
 