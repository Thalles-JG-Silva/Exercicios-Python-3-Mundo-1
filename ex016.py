#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc

n = float(input('Digite um numero Real: '))

print('A porção inteira do número {:.2f} é {}'.format(n,trunc(n)))