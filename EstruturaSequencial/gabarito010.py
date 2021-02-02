"""
IMPORTANTE:
- leia o README e o Enunciado das questões antes de realizar qualquer exercício.
- Antes de copiar as resoluções, tente faze-las primeiro. ; )
- Apoie e agradeça o site de referência.
- Bons estudos.
"""

# Exercício:
""" Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. """

# Resolução1:
c = float(input('Digite a temperatura em graus Celsius: '))
f = c * 1.8 + 32
print(f'A temperatura {c:.2f} graus Celsius, convertida é de {f:.2f} graus Fahrenheit.')

# Resolução2:
c = float(input('Digite a temperatura em graus Celsius: '))
print(f'A temperatura {c:.2f} graus Celsius, convertida é de {c * 1.8 + 32} graus Fahrenheit.')
