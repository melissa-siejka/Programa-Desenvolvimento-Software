def buscaBinaria(lista, x, inicio, fim):
    if inicio > fim:
        return -1
    meio = inicio + (fim - inicio) // 2
    if lista[meio] == x:
        return meio
    elif lista[meio] > x:
        print('Busca na metade inferior')
        return buscaBinaria(lista, x, inicio, meio - 1)
    else:
        print('Busca na metade superior')
        return buscaBinaria(lista, x, meio + 1, fim)

lista_1 = [7,16,26,54,62,68,79,118,144,157,189,191,205]
buscaValor = int(input("Informe o valor para buscar na lista: "))

posicaoLista = buscaBinaria(lista_1, buscaValor, 0, len(lista_1) - 1)

if posicaoLista < 0:
    print(f"Valor {buscaValor} não encontrado.")
else:
    print(f"O valor {buscaValor} está na {posicaoLista + 1}ª posição da lista.")

