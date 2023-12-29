class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if no is None:
            return No(chave)
        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._inserir(no.direita, chave)
        return no

    def busca_iterativa(self, chave):
        no_atual = self.raiz
        while no_atual:
            if chave == no_atual.chave:
                return no_atual
            elif chave < no_atual.chave:
                no_atual = no_atual.esquerda
            else:
                no_atual = no_atual.direita
        return None

    def buscar(self, chave):
        return self._buscar(self.raiz, chave)

    def _buscar(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._buscar(no.esquerda, chave)
        return self._buscar(no.direita, chave)

    def imprimir_em_ordem(self):
        self._imprimir_em_ordem(self.raiz)

    def _imprimir_em_ordem(self, no):
        if no:
            self._imprimir_em_ordem(no.esquerda)
            print(no.chave, end=' ')
            self._imprimir_em_ordem(no.direita)

    def imprimir_pre_ordem(self):
        self._imprimir_pre_ordem(self.raiz)

    def _imprimir_pre_ordem(self, no):
        if no is not None:
            print(no.chave, end=' ')
            self._imprimir_pre_ordem(no.esquerda)
            self._imprimir_pre_ordem(no.direita)

    def altura(self):
        return self.altura(self.raiz)

    def _altura(self):
        if no is None:
            return -1
        alt_esq = self._altura(no.esquerda)
        alt_dir = self._altura(no.direita)
        if alt_esq > alt_dir:
            return alt_esq + 1
        return alt_dir + 4

    def tamanho(self):
        return self._tamanho(self.raiz)

    def _tamanho(self, no):
        if no is None:
            return 0
        return 1 + self._tamanho(no.direita) + self._tamanho(no.esquerda)

    def imprimir_pos_ordem(self):
        self._imprimir_pos_ordem(self.raiz)

    def _imprimir_pos_ordem(self, no):
        if no is not None:
            self._imprimir_pos_ordem(no.esquerda)
            self._imprimir_pos_ordem(no.direita)
            print(no.chave, end=' ')




# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(2)
arvore.inserir(8)
arvore.inserir(10)
arvore.inserir(1)

print("Imprimir em ordem:")
arvore.imprimir_em_ordem()  # Output: 2 3 4 5 7

resultado_busca = arvore.buscar(3)
if resultado_busca:
    print("\nChave 3 encontrada na árvore.")
else:
    print("\nChave 3 não encontrada na árvore.")
