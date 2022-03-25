# 3-Crie um programa em Python que solicite ao usuário a sua idade expressa em anos,
# meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas em dias.
# Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.

# Entrada

anos = int(input("Inserir sua idade expressa em anos:\n"))
meses = int(input("Inserir sua idade expressa em meses:\n"))
dias = int(input("Inserir sua idade expressa em dias:\n"))

# Processamento

idade_em_dias = int(anos*365 + meses*30 + dias)

# Saída

print(f"\nSua idade total expressa em dias é: {idade_em_dias}.")