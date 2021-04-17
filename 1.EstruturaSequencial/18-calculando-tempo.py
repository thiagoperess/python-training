# Exercício 18

# Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), calcule e informe o 
# tempo aproximado de download do arquivo usando este link (em minutos). 

tamanho_arquivo = int(input('Qual o tamanho do arquivo? '))
velocidade_download = int(input('Qual a velocidade? [Mbps] '))

tempo_estimado = (tamanho_arquivo / velocidade_download) * 60

print(f'A velocidade média de download para um arquivo de {tamanho_arquivo}MB com valocidade de {velocidade_download}Mbps é de {tempo_estimado:.0f} minutos')

# print('Tempo aproximado de download: %.0f Minutos ' %((tamanho_arquivo / velocidade_download) * 60))