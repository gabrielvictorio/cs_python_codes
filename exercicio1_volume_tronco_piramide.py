# 1- Faça um programa em Python que calcule e mostre o valor do volume do tronco de
# uma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura do
# tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e
# calcular a seguinte expressão:
# volume =h/3* (Bmaior2 + Bmenor2 + (Bmaior2 * Bmenor2)**0.5)

# Bibliotecas utilizadas

import math

# Entrada

tronco = float(input("Inserir valor do tronco da pirâmide em metros:\n"))
base_menor = float(input("Inserir valor da base menor da pirâmide em metros:\n"))
base_maior = float(input("Inserir valor da base maior da pirâmide em metros:\n"))

# Processamento

area_base_menor = base_menor**2
area_base_maior = base_maior**2

volume_tronco = tronco/3 * (area_base_maior + area_base_menor + math.sqrt(area_base_maior*area_base_menor))

# Saída

print(f"\nO volume do tronco é de {volume_tronco:.3f} m³.")
