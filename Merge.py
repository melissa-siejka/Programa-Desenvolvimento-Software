
# Função merge para unir os elementos das listas A e B
def merge (A,B):
    resultado = []

#Velidação se a lista não está vazia
    while A and B:
        if A[0] < B[0]:
            resultado.append(A.pop(0)) # Função pop remove o último elemento e obter o primeiro elemento da lista
        else:
            resultado.append(B.pop(0))
    while A:
        resultado.append(A.pop(0))

    while B:
        resultado.append(B.pop(0))

    return resultado

# Listas A e B
A = [12, 35, 52, 64]
B = [5, 15, 23, 55, 75]

# Chama a função merge para combinar as listas ordenadas A e B
R = merge(A, B)

# Impressão do resultado ordenado

print("Resultado:", R)
