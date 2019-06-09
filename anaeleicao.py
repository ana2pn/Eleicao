
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
            return 'A arvore esta vazia!'
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

    def preorder(self, no):                     #Exibe os valores dos nós em preordem
        if no is not self.getnil():
            print(no.getvalor(), end= " ")
            self.preorder(no.getesquerdo())
            self.preorder(no.getdireito())


    def posorder(self, no):                     #Exibe os valores dos nós em posordem
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
        while valor.getesquerdo() is not self.getnil():
            valor = valor.getesquerdo()
        return valor

    def maximo (self, valor):
        while valor.getdireito() is not self.getnil():
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

    def predecessor(self, no):
        if no is not None:
            if no.getesquerdo() is not self.getnil() and no.getesquerdo().getvalor() != no.getvalor():
                return self.maximo(no.getesquerdo())

            elif no.getesquerdo() is not self.getnil() and no.getesquerdo().getvalor() == no.getvalor():
                no_2 = no.getesquerdo()
                while no_2.getesquerdo() is not self.getnil() and no_2.getesquerdo().getvalor() == no.getvalor():
                    no_2 = no_2.getesquerdo()
                if no_2.getesquerdo() is not self.getnil():
                    return self.maximo(no_2.getesquerdo())
                else:
                    if no.getpai() != no:
                        return no.getpai()
                    else:
                        self.predecessor(no.getpai())

            else:
                if no.getpai().getvalor() != no.getvalor():
                    return no.getpai()
                else:
                    self.predecessor(no.getpai())


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
    def inserirVP(self, valor):
        no=noh(valor)                               #Cria o objeto do novo no
        pai=self.getraiz()
        if pai is None:                             #Verifica se a árvore esta vazia
            self.setraiz(no)                        #o novo no passa a ser a raiz
            no.setvermelho(False)                   #Faz a raiz ser preta
            no.setdireito(self.getnil())            #direito esquerdo e pai apontam para nil
            no.setesquerdo(self.getnil())
            no.setpai(self.getnil())
        else:                                       #Caso a árvore não esteja vazia
            while True:
                if valor <= pai.getvalor():         #Verifica se o valor do no inserido é menor que o valor da raiz
                    new_pai = pai.getesquerdo()
                    if new_pai is self.getnil():
                        break                        #O laço while é interrompido quando é encontrada uma posicao vazia para o novono
                    else:
                        pai = new_pai
                else:                                #O no inserido é maior que a raiz
                    new_pai = pai.getdireito()
                    if new_pai is self.getnil():
                        break
                    else:
                        pai = new_pai
            no.setpai(pai)                              #Faz o ponteiro do no apontar para o pai do no
            if valor < pai.getvalor():                  #Faz o ponteiro do pai apontar para o no adicionado seja ele esquerdo ou direito
                pai.setesquerdo(no)
            else:
                pai.setdireito(no)
            no.setdireito(self.getnil())                # Faz o ponteiro esquerdo e direito do no folha apontar para nil
            no.setesquerdo(self.getnil())
            self.ajustar_insercao(no)                   #Chama a funcao ajustar_insercao para verificar e balancear a arvore vermelha e preta


    def rotacaoesquerda(self, no):
        y = no.getdireito()                             #Define y como sendo o filho direito do no recebido pela funcao
        no.setdireito(y.getesquerdo())                  #O filho direito do no passa a ser a subarvore esquerda de y
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
            if No.getpai() == No.getpai().getpai().getesquerdo():   #verifica se o pai eh filho esquerdo do passado pela funcao
                y = No.getpai().getpai().getdireito()               #y passa a ser o tio do no que desbalanceou a arvore
                if y.getvermelho():                                 #Verifica se o tio do no eh vermelho
                    No.getpai().setvermelho(False)                  #Faz o pai e o tio do no serem pretos e o avo de no ser vermelho(caso 1)
                    y.setvermelho(False)
                    No.getpai().getpai().setvermelho(True)
                    No = No.getpai().getpai()
                else:                                                #Caso em que o tio do no eh preto, o no e o pai do no sao vermelhos (caso 2)
                    if No == No.getpai().getdireito():               #Verifica se o no eh filho direito do pai do no
                        No = No.getpai()                             #Caso seja, eh executada uma rotacao dupla direita no pai do no
                        self.rotacaoesquerda(No)                     #E caso não seja, apenas executa-se uma rotacao direita simples no avo do no
                    No.getpai().setvermelho(False)                   #O pai do no passa a ser preto
                    No.getpai().getpai().setvermelho(True)           #O avo do no passa a ser vermelho
                    self.rotacaodireita(No.getpai().getpai())
            else:                                                    #Caso em que o pai do no é filho direito do no que foi passado para funcao
                y = No.getpai().getpai().getesquerdo()               #y passa a ser o tio do no passado para funcao
                if y.getvermelho():                                  #Verifica se o tio do no eh vermelho
                    No.getpai().setvermelho(False)                   #Faz o pai e o tio do no serem pretos e o avo de no ser vermelho(caso 1)
                    y.setvermelho(False)
                    No.getpai().getpai().setvermelho(True)
                    No = No.getpai().getpai()
                else:
                    if No == No.getpai().getesquerdo():             #Verifica se o no eh filho esquerdo do pai do no
                        No = No.getpai()                            #Caso seja, eh executada uma rotacao dupla esquerda no pai do no
                        self.rotacaodireita(No)                     #E caso nao seja apenas executa-se uma rotacao esquerda simples no avo do no
                    No.getpai().setvermelho(False)                  #O pai do no passa a ser preto
                    No.getpai().getpai().setvermelho(True)          #O avo do no passa a ser vermelho
                    self.rotacaoesquerda(No.getpai().getpai())
        self.getraiz().setvermelho(False)                           #Depois de todos os ajustes, faz a raiz ser preta, independentemente de qualquer caso


    def remover_rb(self, z):
        if z.getesquerdo() is self.getnil() or z.getdireito() is self.getnil():
            y = z
        else:
            y = self.predecessor(z)
        if y.getesquerdo() is not self.getnil():
            x = y.getesquerdo()
        else:
            x = y.getdireito()
        #x.setpai(y.getpai())                           #Linha que existe no pseudo-código, mas quando descomentada dá erro e comentada funciona
        if y.getpai() is self.getnil():
            self.setraiz(x)
        else:
            if y == y.getpai().getesquerdo():
                y.getpai().setesquerdo(x)
            else:
                y.getpai().setdireito(x)
        if y != z:
            z.setvalor(y.getvalor())
        if y.getvermelho is False:
            self.remover_rb_ajuste(x)
        return y

    def remover_rb_ajuste(self, no_fixup):
        while no_fixup != self.getraiz() and no_fixup.getvermelho() is False:
            if no_fixup == no_fixup.getpai().getesquerdo():
                w = no_fixup.getpai().getdireito()
                if w.getvermelho() is True:
                    w.setvermelho(False)
                    no_fixup.getpai().setvermelho(True)
                    self.rotacaoesquerda(no_fixup.getpai())
                    w = no_fixup.getpai().getdireito()
                if w.getesquerdo().getvermelho() is False and w.getdireito().getvermelho() is False:
                    w.setvermelho(True)
                    no_fixup = no_fixup.getpai()
                else:
                    if w.getdireito().getvermelho() is False:
                        w.getesquerdo().setvermelho(False)
                        w.setvermelho(True)
                        self.rotacaodireita(w)
                        w = no_fixup.getpai().getdireito()
                        w.setvermelho(no_fixup.getpai().getvermelho())
                        no_fixup.getpai().setvermelho(False)
                        w.getdireito().setvermelho(False)
                        self.rotacaoesquerda(no_fixup.getpai())
                        no_fixup = self.getraiz()
            else:
                w = no_fixup.getpai().getesquerdo()
                if w.getvermelho() is True:
                    w.setvermelho(False)
                    no_fixup.getpai().setvermelho(True)
                    self.rotacaodireita(no_fixup.getpai())
                    w = no_fixup.getpai().getesquerdo()
                if w.getdireito().getvermelho() is False and w.getesquerdo().getvermelho() is False:
                    w.setvermelho(True)
                    no_fixup = no_fixup.getpai()
                else:
                    if w.getdireito().getvermelho() is False:
                        w.getdireito().setvermelho(False)
                        w.setvermelho(True)
                        self.rotacaoesquerda(w)
                        w = no_fixup.getpai().getesquerdo()
                        w.setvermelho(no_fixup.getpai().getvermelho())
                        no_fixup.getpai().setvermelho(False)
                        w.getesquerdo().setvermelho(False)
                        self.rotacaodireita(no_fixup.getpai())
                        no_fixup = self.getraiz()
        no_fixup.setvervmelho(False)

arvoreVP = ArvoreVermelhaePreta()
elementos = [35, 21, 32, 12, 23, 54, 11, 31, 40]
for i in elementos:
    arvoreVP.inserirVP(i)
arvoreVP.preorder(arvoreVP.getraiz())

arvoreVP.remover_rb(arvoreVP.procurar(32))
print()
print()
arvoreVP.preorder(arvoreVP.getraiz())