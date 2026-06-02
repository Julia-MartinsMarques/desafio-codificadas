# Recebe o nome de usuário da entrada
namo = input()

# O comando 'set(namo)' cria um conjunto com as letras do nome,
# eliminando automaticamente qualquer repetição.
# O comando 'len()' conta quantos caracteres sobraram.
caracteres_distintos = len(set(namo))

# Se o número de caracteres distintos for par (resto da divisão por 2 é zero),
# então é mulher (converse com ela!).
# Se for ímpar, é homem (IGNORE ele!).
if caracteres_distintos % 2 == 0:
    print("converse com ela!")
else:
    print("IGNORE ele!")