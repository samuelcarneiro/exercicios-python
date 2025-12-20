# Exercício 06
# Crie um algoritmo que leia um número e mostre
# seu dobro, triplo e raiz quadrada
from math import sqrt

numero = int(input('Informe um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = sqrt(numero)

print('Número informado: {}.'.format(numero))
print('Dobro: {}.'.format(dobro))
print('Triplo: {}.'.format(triplo))
print('Raíz quadrada: {}.'.format(int(raiz)))