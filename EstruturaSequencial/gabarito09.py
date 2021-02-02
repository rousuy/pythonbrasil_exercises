"""
IMPORTANTE:
- leia o README e o Enunciado das questões antes de realizar qualquer exercício.
- Antes de copiar as resoluções, tente faze-las primeiro. ; )
- Apoie e agradeça o site de referência.
- Bons estudos.
"""

"""Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre em graus Celsius."""

# Resolução1:
f = float(input('Digite a temperatura em Fahrenheit: '))
c = (f - 32) / 1.8
print(f'A temperatura {f:.1f} Fahrenheit, convertida para graus Celsius é de {c:.2f}.')

# Resolução2:
f = float(input('Digite a temperatura em Fahrenheit: '))
print(f'A temperatura {f:.1f} Fahrenheit, convertida é de {(f - 32) / 1.8:.2f} graus Celsius')
