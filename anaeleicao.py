
class noh:
    def __init__(self, valor):
        self._valor = valor
        self._esquerdo = None
        self._direito = None
        self._pai = None
        self._vermelho = False

    def setvermelho(self, cor=True):
        self._vermelho = cor

    def getvermelho(self):
        return self._vermelho

    def getvalor(self):
        return self._valor

    def setvalor(self, valor):
        self._valor = valor

    def getesquerdo(self):
        return self._esquerdo

    def setesquerdo(self, esquerdo):
        self._esquerdo = esquerdo

    def getdireito(self):
        return self._direito

    def setdireito(self, direito):
        self._direito = direito

    def getpai(self):
        return self._pai

    def setpai(self, pai):
        self._pai = pai


class ArvoredeBuscaBinaria:
    def __init__(self):
        self._raiz = None
        self._nil = None


    def getnil(self):
        return self._nil

    def setnil(self, nil):
        self._nil = nil

    def getraiz(self):
        return self._raiz

    def setraiz(self, raiz):
        self._raiz = raiz

    def __str__(self):
        if self.ehVazio():
            return 'The Tree is empty!'
        else:
            return print("%d"+str(noh.getvalor()))

    def ehVazio(self):
        return self._raiz is None

    def ehfilhodireito(self, no):
        if no is not None:
            if no is not self.getraiz():
                if no.getvalor() == no.getpai().getdireito():
                    return no.getvalor()
        return None

    def ehfilhoesquerdo(self, no):
        if no is not None:
            if no is not self.getraiz():
                if no.getvalor() == no.getpai().getesquerdo():
                    return no.getvalor()
        return None

    def inserir(self, valor):
        novonoh = noh(valor)
        if self.ehVazio():
            self.setraiz(novonoh)
            return novonoh
        i = self._raiz
        while True:
            if valor <= i.getvalor():
                if i.getesquerdo() is None:
                    i.setesquerdo(novonoh)
                    novonoh.setpai(i)
                    break
                else:
                    i = i.getesquerdo()
            else:
                if i.getdireito() is None:
                    i.setdireito(novonoh)
                    novonoh.setpai(i)
                    break
                else:
                    i = i.getdireito()
        return novonoh



    def procurar(self, valor):
        if self.getraiz() == None:
            return None
        i = self.getraiz()
        while i.getvalor() != valor:
            if valor <= i.getvalor():
                i = i.getesquerdo()
            else:
                i = i.getdireito()
            if i == None:
                return None

        return i

    def preorder(self, no):
        if no != None:
            print(no.getvalor(), end= " ")
            self.preorder(no.getesquerdo())
            self.preorder(no.getdireito())


    def posorder(self, no):
        if no != None:
            self.posorder(no.getesquerdo())
            self.posorder(no.getdireito())
            print(no.getvalor(), end=" ")

    def inorder(self, no):
        if no != None:
            self.inorder(no.getesquerdo())
            print(no.getvalor(), end=" ")
            self.inorder(no.getdireito())

    def minimo(self, valor):
        while valor.getesquerdo() is not None:
            valor = valor.getesquerdo()
        return valor

    def maximo (self, valor):
        while valor.getdireito() is not None:
            valor = valor.getdireito()
        return valor

    def sucessor(self, value):
        if value.getdireito() != None:
            return self.minimo(value.getdireito())
        y = value.getpai()
        while y != None and value == y.getdireito():
            value = y
            y = y.getpai()
        return y

    def remover(self, v):
        if v.getesquerdo() == None or v.getdireito() == None:
            y = v
        else:
            y = self.sucessor(v)
        if y.getesquerdo() is not None:
            x = y.getesquerdo()
        else:
            x = y.getdireito()
        if x != None:
            x.setpai(y.getpai())
        if y.getpai() == None:
            self.setraiz(x)
        else:
            if y == y.getpai().getesquerdo():
                y.getpai().setesquerdo(x)
            else:
                y.getpai().setdireito(x)
        if y != v:
            v.setvalor(y.getvalor())
        return y

class ArvoreVermelhaePreta(ArvoredeBuscaBinaria):

    def inserirVP(self, z):
        z = noh(z)
        y = self.getnil()
        x = self.getraiz()

        while x is not self.getnil():
            y = x
            if z.getvalor() < x.getvalor():
                x = x.getesquerda()
            else:
                x = x.direita()

        z.getpai().setvalor(y)
        if y == self.getnil():
            self.setraiz(z)
        elif z.getvalor() < x.getvalor():
            y.setesquerdo(z)
        else:
            y.setdireito(z)
        z.setesquerdo(self.getnil())
        z.setdireito(self.getnil())
        z.setvermelho(True)
        self.ajustar_insercao(z)

    def rotacaoesquerda(self, x):
        y = x.getdireito()
        x.setdireito(y.getesquerdo())
        if y.getesquerdo() is not None:
            y.getesquerdo().setpai(x)
        y.setpai(x.getpai())
        if x.getpai() is None:
            self.setraiz(y)
        else:
            if self.ehfilhoesquerdo(x):
                x.getpai().setesquerdo(y)
            else:
                x.getpai().setdireito(y)
        y.setesquerdo(x)
        x.setpai(y)

    def rotacaodireita(self, y):
        x = y.getesquerdo()
        y.setesquerdo(x.getdireito())
        if x.getdireito() is not None:
            x.getdireito().setpai(y)
        x.setpai(y.getpai())
        if y.getpai() is None:
            self.setraiz(x)
        else:
            if self.ehfilhodireito(y):
                y.getpai().setdireito(x)
            else:
                y.getpai().setesquerdo(x)
        x.setdireito(y)
        y.setpai(x)

    def ajustar_insercao(self, z):
        while z.getpai().getvermelho():
            if z.pai() == z.getpai().getpai().getesquerdo():
                y = z.getpai().getpai().getdireito()
                if y.getvermelho():
                    z.getpai().setvermelho(False)
                    y.setvermelho(False)
                    z.getpai().getpai().setvermelho(True)
                    z = z.getpai().getpai()
                else:
                    if z == z.getpai().getdireita():
                        z = z.getpai()
                        self.rotacaoesquerda(z)
                    z.getpai().setvermelho(False)
                    z.getpai().getpai().setvermelho(True)
                    self.rotacaodireita(z.getpai().getpai())
            else:
                y = z.getpai().getpai().getesquerdo()
                if y.getvermelho():
                    z.getpai().setvermeho(False)
                    y.setvermelho(False)
                    z.getpai().getpai().setvermleho(True)
                    z = z.getpai().getpai()
                else:
                    if z == z.getpai().getesquerdo():
                        z = z.getpai()
                        self.rotacaodireita(z)
                    z.getpai().setvermelho(False)
                    z.getpai().getpai().setvermelho(True)
                    self.rotacaoesquerda(z.getpai().getpai())
        self._raiz().setvermelho(False)

arvoreVP = ArvoreVermelhaePreta()
elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in elementos:
    arvoreVP.inserirVP(i)
arvoreVP.preorder(arvoreVP.getraiz())
