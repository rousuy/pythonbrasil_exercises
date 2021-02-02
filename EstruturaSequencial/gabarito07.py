"""
 IMPORTANTE:
 - leia o README e o Enunciado das questões antes de realizar qualquer exercício.
 - Antes de copiar as resoluções, tente faze-las primeiro. ; )
 - Apoie e agradeça o site de referência.
 - Bons estudos.
"""

# Exercício:
"""
Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
Obs.: Sabemos que para calcular a área de um quadrado basta multiplicar sua Base x Altura, ou Lado².
"""

# Resolução1:
base = int(input('Digite um valor (em metros) da base de um quadrado a ser calculado sua área: '))
altura = int(input('Digite um valor (em metros) da altura de um quadrado a ser calculado sua área: '))
area = base * altura
print(f'A área do quadrado com base de {base}m e {altura}m de altura é de {area}m quadrados. Seu dobro é de {area * 2}m'
      f' quadrados.')


# Resolução2:
base = int(input('Digite um valor (em metros) da base de um quadrado a ser calculado sua área: '))
altura = int(input('Digite un valor (em metros) da altura de um quadrado a ser calculado sua área: '))
print(f'A área do quadrado com {base}m de base e {altura}m de altura é de {base * altura}m quadrados. Seu dobro é de '
      f'{base * altura * 2}m quadrados.')
