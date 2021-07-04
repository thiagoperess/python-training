# Exercício 18

# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a monthma é uma data válida.

day = int( input('Dia: ') )
month = int( input('Mês: ') )
year = int( input('Ano: ') )

valid = False

if( month==1 or month==3 or month==5 or month==7 or \
    month==8 or month==10 or month==12):
    if(day<=31):
        valid = True

elif( month==4 or month==6 or month==9 or month==11):
    if(day<=30):
        valid = True
        
elif month==2:
    if (year%4==0 and year%100!=0) or (year%400==0):
        if(day<=29):
            valid = True
    elif(day<=28):
            valid = True

if(valid):
    print('Data válida')
else:
    print('Inválida')