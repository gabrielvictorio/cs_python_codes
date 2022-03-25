# 5- Faça uma programa em Python que peça do usuário um valor em graus para um
# ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o seno,
# cosseno e tangente deste ângulo.

# Bibliotecas utilizadas:
import math

# Entrada

valor_graus = float(input("Inserir valor em grau de um ângulo:\n"))

# Processamento

valor_radians = math.radians(valor_graus)
valor_seno = math.sin(valor_radians)
valor_cosseno = math.cos(valor_radians)
valor_tangente = math.tan(valor_radians)

# Saída

print(f"\nValor do seno: {valor_seno:.3f}.\nValor do cosseno: {valor_cosseno:.3f}."
      f"\nValor da tangente: {valor_tangente:.3f}")
