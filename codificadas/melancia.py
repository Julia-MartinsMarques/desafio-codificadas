# Solicita o peso da melancia ao usuário
peso = int(input("Digite o peso da melancia: "))

# Calcula o resto da divisão por 2
resto = peso % 2

# Verifica se o resto é igual a 0 (se o número é par)
if resto == 0:
    print("SIM")
else:
    print("NÃO")