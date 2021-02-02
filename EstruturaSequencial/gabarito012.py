"""
IMPORTANTE:
- leia o README e o Enunciado das questões antes de realizar qualquer exercício.
- Antes de copiar as resoluções, tente faze-las primeiro. ; )
- Apoie e agradeça o site de referência.
- Bons estudos.
"""

# Exercício:
"""
Tendo como dados de entrada a altura de um pessoa, construa um algoritmo que calcule seu peso ideal usando a seguinte
fórmula: `(72.7 * altura) - 58` (calculo de IMC).
"""

# Resolução1:
altura = float(input('Digite sua altura: '))
peso_ideal = (72.7 * altura) - 58
print(f'Com altura de {altura}, seu peso ideal é de: {peso_ideal:.2f}')

# Resolução2:
altura = float(input('Digite sua altura: '))
print(f'Com altura de {altura}, seu peso ideal é de: {round((72.7 * altura) - 58)}')
