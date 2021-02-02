"""
IMPORTANTE:
- leia o README e o Enunciado das questões antes de realizar qualquer exercício.
- Antes de copiar as resoluções, tente faze-las primeiro. ; )
- Apoie e agradeça o site de referência.
- Bons estudos.
"""

# Exercício:
"""
Tendo como dado de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:
    1. Para homens: `(72.7 * altura) - 58`;
    2. Para mulheres: `(62.1 * altura) - 44.7`.
"""

# Resolução1:
altura = float(input('Digite sua altura: '))
peso_ideal_h = (72.7 * altura) - 58
peso_ideal_f = (62.1 * altura) - 44.7
print(f'Com altura de: {altura}, o peso ideal para homens é de: {peso_ideal_h:.2f} quilos, e para mulheres é de:'
      f'{peso_ideal_f:.2f} quilos.')

# Resolução2:
altura = float(input('Digite sua altura: '))
print(f'Com altura de {altura}, o peso ideal para homens é de: {round((72.7 * altura) - 58)} quilos, e para mulheres é '
      f'{round((62.1 * altura) - 44.7)} quilos.')
