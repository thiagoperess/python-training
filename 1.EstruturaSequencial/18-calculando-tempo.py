# Exercício 18

# Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), calcule e informe o 
# tempo aproximado de download do arquivo usando este link (em minutos). 

file_size = int(input('Tamanho do arquivo? '))
download = int(input('Velocidade em [Mbps]: '))

time = (file_size / download) * 60

print(f'A velocidade download para {file_size}MB \
        com {download}Mbps é de {time:.0f} minutos')

