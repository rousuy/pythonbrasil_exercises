"""
IMPORTANTE:
- leia o README e o Enunciado das questões antes de realizar qualquer exercício.
- Antes de copiar as resoluções, tente faze-las primeiro. ; )
- Apoie e agradeça o site de referência.
- Bons estudos.
"""

# Exercício:
"""
Faça um programa que pergunte quanto você ganha por hora, e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
"""

# Resolução1:
salario_hora = int(input('Digite o valor ganho por hora trabalhada: '))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas no Mês: '))
salario = salario_hora * horas_trabalhadas
print(f'No mẽs, você trabalhou {horas_trabalhadas} horas. Portanto seu salário é de R${salario:.2f}.')

# Resolução2:
salario_hora = int(input('Digite o valor ganho por hora trabalhada: '))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas no mês: '))
print(
      f'''No mês, você trabalhou {horas_trabalhadas} horas.Portanto seu salário é de R$
      {salario_hora * horas_trabalhadas:.2f}.'''
      )
