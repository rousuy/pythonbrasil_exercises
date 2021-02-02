"""
IMPORTANTE:
- leia o README e o Enunciado das questões antes de realizar qualquer exercício.
- Antes de copiar as resoluções, tente faze-las primeiro. ; )
- Apoie e agradeça o site de referência.
- Bons estudos.
"""

# Exercício:
"""
Faça um programa que peça o raio de um círculo, calcule e mostre a sua área.
Obs.: Sabemos que para calcular a área de um círculo temos a fórmula:
- área = ?
- raio = ?
- pi = 3.14
a = pi * r²
"""

# Resolução1:
r = int(input('Digite um valor (em metros) do raio, para calcular a área de seu círculo: '))
a = 3.14 * r * r
print(f'A área do círculo é de aproximadamente {a} metros ao quadrado.')


# Resolução2:
r = int(input('Digite o valor (em metros) do raio, para calcular a área de seu círculo: '))
print(f'A área do círculo é de aproximadamente {3.14 * r**2} metros ao quadrado.')
