# Exercício 16

# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

print('\nSEQUÊNCIA FIBONACCI\n')

last = 1
penlast = 1
print(penlast, '→ ', end='')
print(last, end='')
term = 0

while term < 500:
    term = last + penlast
    penlast = last
    last = term
    if term < 500:
        print(f' → {term}', end='')
    else:
        print(' → FIM')
        print('\nO proximo valor será maior que 500')
