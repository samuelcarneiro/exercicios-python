# Exercício 07
# Desenvolva um programa que leia duas notas de um aluno,
# calcule e mostre sua média 

nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))
media = (nota1 + nota2)/2

print('A média do aluno é: {:.2f}'.format(media))