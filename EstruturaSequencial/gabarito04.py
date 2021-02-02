"""
IMPORTANTE:
- leia o README e o Enunciado das questões antes de realizar qualquer exercício.
- Antes de copiar as resoluções, tente faze-las primeiro. ; )
- Apoie e agradeça o site de referência.
- Bons estudos.
"""

"""Faça um programa que peça as 4 notas bimestrais e mostre a média.
   Obs.: As notas não são obrigatoriamente números inteiros."""

# Resolução1:
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média dos bimestres é de: {media} pontos.')

# Resolução2:
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))
print(f'A média dos bimestres é de: {(nota1 + nota2 + nota3 + nota4) / 4} pontos.')
