# 4-Escreva um programa em Python para calcular o valor de uma prestação em atraso
# (prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de
# multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o
# valor da prestação atualizado, sabendo que:
# prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

# Entrada

valor_prestacao = float(input("Inserir valor da prestação:\n"))
multa = int(input("Inserir a porcentagem da multa:\n"))
qtde_dias = int(input("Inserir a quantidade de dias em atraso:\n"))

# Processamento

prestacao_atualizada = valor_prestacao + (valor_prestacao * (multa/100) * qtde_dias)

# Saída

print(f"\nO valor da prestação atualizada é de: {prestacao_atualizada:.2f}.")