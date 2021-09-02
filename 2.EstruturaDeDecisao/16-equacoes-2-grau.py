# Exercício 16

# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# delta = b**2 - (4*a*c)
# raiz = (-b +ou- (delta**(1/2)))/(2*a)

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = 0
raizUm = 0
raizDois = 0

if a == 0:
	print("A equação apresentada não é do segundo grau. O programa será encerrado!")

else:
	print("Calculando delta...")
	delta = ((b ** 2) - (4 * a * c))
	
	if delta == 0:
		print("A equação possui apenas uma raiz que é: ")
		raizUm = ((-b) + (delta ** (1 / 2)) / (2 * a))
		print(raizUm)
	else:
		raizUm = ((-b) + (delta ** (1 / 2)) / (2 * a))
		raizDois = ((-b) - (delta ** (1 / 2)) / (2 * a))
		print("A equação possui duas raizes que são:", raizUm, "e", raizDois)

