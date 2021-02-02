"""
IMPORTANTE:
- leia o README e o Enunciado das questões antes de realizar qualquer exercício.
- Antes de copiar as resoluções, tente faze-las primeiro. ; )
- Apoie e agradeça o site de referência.
- Bons estudos.
"""

# Exercício:
"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    1. O produto do dobro do primeiro com metade do segundo.
    2. A soma do triplo do primeiro com terceiro
    3. O terceiro elevado ao cubo.
"""

# Resolução:
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))
print(f'R: O produto do dobro do primeiro com metade do segundo é: {int(num1 * 2 * num2 / 2)}.')
print(f'R: A soma do triplo do primeiro com o terceiro é: {int(num1 * 3 + num3)}.')
print(f'R: O terceiro elevado a cubo é: {num3 ** 3:.0f}.')
