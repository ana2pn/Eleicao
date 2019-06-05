class noh:
    def __init__(self, valor):
        self._valor = valor
        self._esquerdo = None
        self._direito = None
        self._pai = None

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

