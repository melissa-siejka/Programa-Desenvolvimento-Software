## Validador de Expressões
# Conceito:
        # Permitido usar os caracteres () [] {}
        # Serve para avaliar se a utilização se a utilização dos caracteres está adequada.
        # POP remove o ultimo elemento

class Pilha:
    def __init__(self):
        self.items = []

    def vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.items.pop()
        else:
            return None

    def topo(self):
        if not self.vazia():
            return self.items[-1]
        else:
            return None

    def tamanho(self):
        return len(self.items)



def ValidadorExpressao(expressao):
    pilha = Pilha()
    abreExpressao = "({["
    fechaExpressao = ")}]"

    for a in expressao:
        if a in abreExpressao:
            pilha.empilhar(a)
        elif a in fechaExpressao:
            topo = pilha.desempilhar()
            if topo is None or abreExpressao.index(topo) != fechaExpressao.index(a):
                return False

    return pilha.vazia()




expressao = '((4X5)+1{4[3+2]-5}5+)2)'
resultado = ValidadorExpressao(expressao)
print(resultado)
