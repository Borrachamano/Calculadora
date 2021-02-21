import os
print('='*20)
print('Calculadora')
print('='*20)
print()
print('Menu:\n[1]Adição \n[2]subtração \n[3]Multiplicação \n[4]divisão \n[5]Potencia \n[6]exit')
print('')
print("Escolha uma das opções:")
menu = input('>> ')

if menu == '1':
	print('='*20)
	print('Adição')
	print('='*20)
	print('Escolha o numero desejado:')
	n1 = int(input('>> '))
	print('Digite outro valor: ')
	n2 = int(input('>> '))
	r = n1 + n2
	print('A soma vale > {}'.format(r))

elif menu == '2':
	print('='*20)
	print('Subtração')
	print('='*20)
	print('Digite o valor desejado: ')
	n1 = int(input('>> '))
	print('Digite outro valor:')
	n2 = int(input('>> '))
	r = n1 - n2
	print('A subtração vale > {}'.format(r))

elif menu == '3':
	print('='*20)
	print('Multiplicação')
	print('='*20)
	print('Digite o valor desejado: ')
	n1 = int(input('>> '))
	print('Digite outro valor: ')
	n2 = int(input('>> '))
	r = n1 * n2
	print('A multiplicação vale > {}'.format(r))

elif menu == '4':
	print('='*20)
	print('Divisão')
	print('='*20)
	print('Digite o valor desejado: ')
	n1 = int(input('>> '))
	print('Digite outro valor: ')
	n2 = int(input('>> '))
	r = n1 

elif menu == '5':
	print('='*20)
	print('Potencia')
	print('='*20)
	print('Escolha o valor desejado: ')
	n1 = int(input('>> '))
	print('Digite outro valor: ')
	n2 = int(input('>> '))
	r = n1 ** n2
	print('A sua potencia é > {}'.format(r))

elif menu == '6':
	print('='*20)
	print('Voce saiu do prorama!')
	print('='*20)
	os.system('exit')
else:
	print('-'*30)
	print('caractere invalida')
	print('-'*30)
