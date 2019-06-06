
class noh:
    def __init__(self, valor):
        self._valor = valor
        self._esquerdo = None
        self._direito = None
        self._pai = None
        self._vermelho = True

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

    def __str__(self):
        nod=('no: %i'%self.getvalor())
        return nod


class Nil():
    def __init__(self):
        self._valor = None
        self._vermelho = False
    def getvermelho(self):
        return False

    def __str__(self):
        return 'None preto'

class ArvoredeBuscaBinaria:
    def __init__(self):
        self._raiz = None
        self._nil = Nil()


    def getnil(self):
        return self._nil

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
                if no == no.getpai().getdireito():
                    return True
        return None

    def ehfilhoesquerdo(self, no):
        if no is not None:
            if no is not self.getraiz():
                if no == no.getpai().getesquerdo():
                    return True
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
        if no is not self.getnil():
            print(no.getvalor(), end= " ")
            self.preorder(no.getesquerdo())
            self.preorder(no.getdireito())


    def posorder(self, no):
        if no is not self.getnil():
            self.posorder(no.getesquerdo())
            self.posorder(no.getdireito())
            print(no.getvalor(), end=" ")

    def inorder(self, no):
        if no is not self.getnil():
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

        while x is not None:
            y = x
            if z.getvalor() < x.getvalor():
                x = x.getesquerdo()
            else:
                x = x.direito()

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

    def inserir_jaime(self, valor):
        no=noh(valor)
        pai=self.getraiz()
        if pai is None:
            self.setraiz(no)
            no.setvermelho(False)
            no.setdireito(self.getnil())
            no.setesquerdo(self.getnil())
            no.setpai(self.getnil())
        else:
            while True:
                if valor<=pai.getvalor():
                    new_pai=pai.getesquerdo()
                    if new_pai is self.getnil():
                        break
                    else:
                        pai=new_pai
                else:
                    new_pai = pai.getdireito()
                    if new_pai is self.getnil():
                        break
                    else:
                        pai=new_pai
            no.setpai(pai)
            if valor<pai.getvalor():
                pai.setesquerdo(no)
            else:
                pai.setdireito(no)
            no.setdireito(self.getnil())
            no.setesquerdo(self.getnil())

            self.ajustar_insercao(no)
    def rotacaoesquerda(self, no):
        y = no.getdireito()
        no.setdireito(y.getesquerdo())
        if y.getesquerdo() is not self.getnil():
            y.getesquerdo().setpai(no)
        y.setpai(no.getpai())
        if no.getpai() is self.getnil():
            self.setraiz(y)
        else:
            if self.ehfilhoesquerdo(no):
                no.getpai().setesquerdo(y)
            else:
                no.getpai().setdireito(y)
        y.setesquerdo(no)
        no.setpai(y)

    def rotacaodireita(self, y):
        x = y.getesquerdo()
        y.setesquerdo(x.getdireito())
        if x.getdireito() is not self.getnil():
            x.getdireito().setpai(y)
        x.setpai(y.getpai())
        if y.getpai() is self.getnil():
            self.setraiz(x)
        else:
            if self.ehfilhodireito(y):
                y.getpai().setdireito(x)
            else:
                y.getpai().setesquerdo(x)
        x.setdireito(y)
        y.setpai(x)

    def ajustar_insercao(self, No):
        while No.getpai().getvermelho():
            if No.getpai() == No.getpai().getpai().getesquerdo(): #se o pai for filho esq
                y = No.getpai().getpai().getdireito()# tio
                if y.getvermelho():
                    No.getpai().setvermelho(False)
                    y.setvermelho(False)
                    No.getpai().getpai().setvermelho(True)
                    No = No.getpai().getpai()
                else:
                    if No == No.getpai().getdireito():
                        No = No.getpai()
                        self.rotacaoesquerda(No)
                    No.getpai().setvermelho(False)
                    No.getpai().getpai().setvermelho(True)
                    self.rotacaodireita(No.getpai().getpai())
            else:
                y = No.getpai().getpai().getesquerdo()
                if y.getvermelho():
                    No.getpai().setvermelho(False)
                    y.setvermelho(False)
                    No.getpai().getpai().setvermelho(True)
                    No = No.getpai().getpai()
                else:
                    if No == No.getpai().getesquerdo():
                        No = No.getpai()
                        self.rotacaodireita(No)
                    No.getpai().setvermelho(False)
                    No.getpai().getpai().setvermelho(True)
                    self.rotacaoesquerda(No.getpai().getpai())
        self.getraiz().setvermelho(False)

arvoreVP = ArvoreVermelhaePreta()
elementos = [35,21,32,12,23,54,11,31,40]
for i in elementos:
    arvoreVP.inserir_jaime(i)
arvoreVP.preorder(arvoreVP.getraiz())
