class noh:
    def __init__(self, valor, nome=None):
        self._valor = valor
        self._esquerdo = None
        self._direito = None
        self._pai = None
        self._vermelho = True
        self._nome = nome

    def getnome(self):
        return self._nome

    def setnome(self, nome):
        self._nome = nome

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
        nod = ('no: %i' % self.getvalor())
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
            return print("%d" + str(noh.getvalor()))

    def ehVazio(self):  # função que verifica se a árvore está vazia
        return self._raiz is None

    def ehfilhodireito(self, no):  # funcao que verifica se um um no eh filho direito
        if no is not None:
            if no is not self.getraiz():
                if no == no.getpai().getdireito():
                    return True
        return None

    def ehfilhoesquerdo(self, no):  # funcao que verifica se um no eh filho esquerdo
        if no is not None:
            if no is not self.getraiz():
                if no == no.getpai().getesquerdo():
                    return True
        return None

    def inserir(self, valor, nome=None):  # funcao que insere um no na arvore
        # global cont                                             #Variavel usada para contar a quantidade de nós da arvore
        novonoh = noh(valor,
                      nome)  # primeiramente verifica se a árvore esta vazia, se estiver o no passa a ser a raiz da arvore
        if self.ehVazio():
            self.setraiz(novonoh)
            return novonoh
        i = self._raiz
        while True:  # Laço que fará as verificações abaixo enquanto o no não for inserido
            if valor < i.getvalor():  # Verifica se o no inserido éh menor que a raiz
                if i.getesquerdo() is None:  # Verifica se o filho esquerdo da raiz eh none
                    i.setesquerdo(novonoh)  # Se for none, o no eh inserido no local onde o none foi encontrado
                    novonoh.setpai(i)  # O ponteiro do novo no passa a apontar para o seu pai
                    break
                else:
                    i = i.getesquerdo()  # Caso o lado esquerdo da raiz não seja none, o no referencia passa a ser o no esquerdo da raiz
            else:  # Caso em que o no inserido eh maior que a raiz
                if i.getdireito() is None:  # Verifica se o no do lado direito da raiz eh none
                    i.setdireito(novonoh)  # Se for ponteiro da raiz passa a apontar para o novono
                    novonoh.setpai(i)  # E o novo no passa a apontar para a raiz
                    break
                else:
                    i = i.getdireito()  # Caso o no do lado direito da raiz nao seja none, o no referencia passa a ser o no direito
        # cont+=1
        return novonoh

    def procurarAB(self, valor):  # Função que irá receber um valor e retornar o no se ele existir na árvore
        if self._raiz is None:  # Se a raiz for vazia, significa que a arvore está vazia e a funcao retorna None
            return None
        i = self._raiz  # A raiz da árvore passa a ser a referencia inicial
        while i != None:
            if valor < i.getvalor():  # Se o valor procurado é menor que o valor da raiz(inicialmente)
                i = i.getesquerdo()  # A função ira procurar o valor do lado esquerdo da árvore
            elif valor > i.getvalor():  # Caso contrário, a função irá procurar o valor do lado direito da arvore
                i = i.getdireito()
            elif valor == i.getvalor():  # Caso encontre irá retornar o no cujo valor é igual ao valor procurado
                return i
            elif i is None:
                return None

    def preorder(self, no):  # Exibe os valores dos nós em preordem
        if no is not None:
            print(no.getvalor(), end=" ")
            self.preorder(no.getesquerdo())
            self.preorder(no.getdireito())

    def posorder(self, no):  # Exibe os valores dos nós em posordem
        if no is not None:
            self.posorder(no.getesquerdo())
            self.posorder(no.getdireito())
            print(no.getvalor(), end=" ")

    def inorder(self, no):
        if no is not None:
            self.inorder(no.getesquerdo())
            print(no.getvalor(), end=" ")
            self.inorder(no.getdireito())

    def minimo(self, valor):
        while valor.getesquerdo() is not self.getnil():
            valor = valor.getesquerdo()
        return valor

    def maximo(self, valor):
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

    def remover(self, v):  # função que remove um nó da arvore, v é o no que será removido
        if v.getesquerdo() == None or v.getdireito() == None:  # Verifica se v possui no máximo um filho
            y = v  # Caso v possua no máximo 1 filho y passa a ser igual a v
        else:
            y = self.sucessor(v)  # Caso v possua dois filhos, fazemos y ser igual ao sucessor de v
        if y.getesquerdo() is not None:  # Verifica se o sucessor de v (y), possui filho esquerdo
            x = y.getesquerdo()  # Se possuir, x passa a ser o filho esquerdo de y
        else:
            x = y.getdireito()  # Se não possuir filho esquerdo, x passa a ser filho direito de y
        if x != None:  # Verifica se x é diferente de vazio
            x.setpai(y.getpai())  # Se for, o pai de x passa a ser o pai de y
        if y.getpai() == None:  # Se y não tiver pai, significa que y é a raiz então a raiz passará a ser x
            self.setraiz(x)
        else:  # Caso y não seja a raiz
            if y == y.getpai().getesquerdo():  # Caso y seja filho esquerdo de algum no
                y.getpai().setesquerdo(x)  # Então x passará a ter toda a subarvore esquerda que era de y
            else:
                y.getpai().setdireito(x)
        if y != v:
            v.setvalor(y.getvalor())  # Caso a condicao seja atendida, o valor do no de v passa a ter o valor do no de y
        return y


class ArvoreVermelhaePreta(ArvoredeBuscaBinaria):
    def inserirVP(self, valor):
        no = noh(valor)  # Cria o objeto do novo no
        pai = self.getraiz()  # Inicialmente a raiz passa ser a referência principal da arvore
        if pai is None:  # Verifica se a árvore esta vazia
            self.setraiz(no)  # o novo no passa a ser a raiz
            no.setvermelho(False)  # Faz a raiz ser preta
            no.setdireito(self.getnil())  # direito esquerdo e pai apontam para nil
            no.setesquerdo(self.getnil())
            no.setpai(self.getnil())
        else:  # Caso a árvore não esteja vazia
            while True:
                if valor <= pai.getvalor():  # Verifica se o valor do no inserido é menor que o valor da raiz
                    new_pai = pai.getesquerdo()  # Caso seja, a referencia da arvore passa a ser o new_pai como lado esquerdo da raiz
                    if new_pai is self.getnil():
                        break  # O laço while é interrompido quando é encontrada uma posicao vazia para o novono
                    else:
                        pai = new_pai
                else:  # O no inserido é maior que a raiz
                    new_pai = pai.getdireito()
                    if new_pai is self.getnil():
                        break
                    else:
                        pai = new_pai
            no.setpai(pai)  # Faz o ponteiro do no apontar para o pai do no
            if valor < pai.getvalor():  # Faz o ponteiro do pai apontar para o no adicionado seja ele esquerdo ou direito
                pai.setesquerdo(no)
            else:
                pai.setdireito(no)
            no.setdireito(self.getnil())  # Faz o ponteiro esquerdo e direito do no folha apontar para nil
            no.setesquerdo(self.getnil())
            self.ajustar_insercao(
                no)  # Chama a funcao ajustar_insercao para verificar e balancear a arvore vermelha e preta

    def procurarVP(self, valor):  # Função que irá receber um valor e retornar o no se ele existir na árvore
        if self._raiz is None:  # Se a raiz for vazia, significa que a arvore está vazia e a funcao retorna None
            return None
        i = self._raiz  # A raiz da árvore passa a ser a referencia inicial
        while i != self._nil:
            if valor < i.getvalor():  # Se o valor procurado é menor que o valor da raiz(inicialmente)
                i = i.getesquerdo()  # A função ira procurar o valor do lado esquerdo da árvore
            elif valor > i.getvalor():  # Caso contrário, a função irá procurar o valor do lado direito da arvore
                i = i.getdireito()
            elif valor == i.getvalor():  # Caso encontre irá retornar o no cujo valor é igual ao valor procurado
                return i
            elif i is None:
                return None

    def preorderVP(self, no):  # Exibe os valores dos nós em preordem
        if no is not self.getnil():
            print(no.getvalor(), end=" ")
            self.preorderVP(no.getesquerdo())
            self.preorderVP(no.getdireito())

    def posorderVP(self, no):  # Exibe os valores dos nós em posordem
        if no is not self.getnil():
            self.posorderVP(no.getesquerdo())
            self.posorderVP(no.getdireito())
            print(no.getvalor(), end=" ")

    def inorderVP(self, no):
        if no is not self.getnil():
            self.inorderVP(no.getesquerdo())
            print(no.getvalor(), end=" ")
            self.inorderVP(no.getdireito())

    def rotacaoesquerda(self, no):
        y = no.getdireito()  # Define y como sendo o filho direito do no recebido pela funcao
        no.setdireito(y.getesquerdo())  # O filho direito do no passa a ser a subarvore esquerda de y
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

    def rotacaodireita(self, y):  # Recebe um no que será rotacionado
        x = y.getesquerdo()  # Define x como sendo filho esquerdo do no recebido pela funcao
        y.setesquerdo(x.getdireito())  # O filho esquerdo de y passa a ser o filho direito de x
        if x.getdireito() is not self.getnil():  # Verifica se o no direito de x não eh nil
            x.getdireito().setpai(y)  # Se nao for nil o pai do no direito de x passa a ser y
        x.setpai(y.getpai())  # O pai direito de x passa a ser y
        if y.getpai() is self.getnil():  # Se o pai de y for nil, x passa a ser a raiz da arvore
            self.setraiz(x)
        else:  # Caso o pai de y não seja nil,a funcao ira verificar se y eh filho esquerdo ou direito de algum no
            if self.ehfilhodireito(y):
                y.getpai().setdireito(x)  # Se for filho direito, o filho direito do pai de y passa a ser x
            else:
                y.getpai().setesquerdo(x)
        x.setdireito(y)  # o filho direito de x passa a ser y
        y.setpai(x)  # e o pai de y passa a ser x

    def ajustar_insercao(self, No):
        while No.getpai().getvermelho():
            if No.getpai() == No.getpai().getpai().getesquerdo():  # verifica se o pai eh filho esquerdo do passado pela funcao
                y = No.getpai().getpai().getdireito()  # y passa a ser o tio do no que desbalanceou a arvore
                if y.getvermelho():  # Verifica se o tio do no eh vermelho
                    No.getpai().setvermelho(
                        False)  # Faz o pai e o tio do no serem pretos e o avo de no ser vermelho(caso 1)
                    y.setvermelho(False)
                    No.getpai().getpai().setvermelho(True)
                    No = No.getpai().getpai()
                else:  # Caso em que o tio do no eh preto, o no e o pai do no sao vermelhos (caso 2)
                    if No == No.getpai().getdireito():  # Verifica se o no eh filho direito do pai do no
                        No = No.getpai()  # Caso seja, eh executada uma rotacao dupla direita no pai do no
                        self.rotacaoesquerda(
                            No)  # E caso não seja, apenas executa-se uma rotacao direita simples no avo do no
                    No.getpai().setvermelho(False)  # O pai do no passa a ser preto
                    No.getpai().getpai().setvermelho(True)  # O avo do no passa a ser vermelho
                    self.rotacaodireita(No.getpai().getpai())
            else:  # Caso em que o pai do no é filho direito do no que foi passado para funcao
                y = No.getpai().getpai().getesquerdo()  # y passa a ser o tio do no passado para funcao
                if y.getvermelho():  # Verifica se o tio do no eh vermelho
                    No.getpai().setvermelho(
                        False)  # Faz o pai e o tio do no serem pretos e o avo de no ser vermelho(caso 1)
                    y.setvermelho(False)
                    No.getpai().getpai().setvermelho(True)
                    No = No.getpai().getpai()
                else:
                    if No == No.getpai().getesquerdo():  # Verifica se o no eh filho esquerdo do pai do no
                        No = No.getpai()  # Caso seja, eh executada uma rotacao dupla esquerda no pai do no
                        self.rotacaodireita(
                            No)  # E caso nao seja apenas executa-se uma rotacao esquerda simples no avo do no
                    No.getpai().setvermelho(False)  # O pai do no passa a ser preto
                    No.getpai().getpai().setvermelho(True)  # O avo do no passa a ser vermelho
                    self.rotacaoesquerda(No.getpai().getpai())
        self.getraiz().setvermelho(
            False)  # Depois de todos os ajustes, faz a raiz ser preta, independentemente de qualquer caso

    def remover_rb(self, z):  # função que remove um no da arvore vermelha e preta, z eh o no que sera removido
        if z.getesquerdo() is self.getnil() or z.getdireito() is self.getnil():  # Verifica se z possui no maximo 1 filho
            y = z  # Caso z tenha no maximo 1 filho, y passa a ser igual a z
        else:  # Caso z possua dois filhos procura-se o predecessor de z e atribui-se o predecessor de z a y
            y = self.predecessor(z)
        if y.getesquerdo() is not self.getnil():  # Verifica se o predecessor existe(não éh vazio)
            x = y.getesquerdo()  # Se existir, x passa a ser o filho esquerdo de y
        else:
            x = y.getdireito()  # Caso contrario x passa a ser o filho direito de y
        if x is not self.getnil():  # Verifica se x definido acima nao eh vazio
            x.setpai(y.getpai())  # Se x não for vazio, o pai de x passa a ser o pai do predecessor de z (pai de y)
        if y.getpai() is self.getnil():  # Caso o pai do predecessor seja vazio, x passa a ser a raiz da arvore
            self.setraiz(x)
        else:  # Caso contrario, verifica se y é filho esquerdo de algum no
            if y == y.getpai().getesquerdo():  # Se for o irmao de y passa a ser x
                y.getpai().setesquerdo(x)
            else:
                y.getpai().setdireito(x)
        if y != z:
            z.setvalor(y.getvalor())
        if y.getvermelho is False:  # Função chamada quando o noh foi removido foi preto para ajustar a arvore vermelha e preta para que
            self.remover_rb_ajuste(x)  # todas as propriedades da arvore vermelha e preta sejam mantidas
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


import random
from random import randint

arvore_de_eleitores = ArvoreVermelhaePreta()  # Objeto instanciado para representar a arvore de eleitores
arvore_de_votacao = ArvoredeBuscaBinaria()  # Objeto instanciado para representar a arvore de votacao
olhou = False
candidato_sem_repeticao, candidato_qntVotos, voto, todos_candidatos = [], [], [], []


def IniciarMenu():  # Menu principal do programa
    print("☆" * 25)
    print("\t\tSistema de Eleição")
    print("☆" * 25)
    print()
    print("1- Titulos")
    print("2- Votação")
    print("Digite o número da sua opção: ", end="")
    op_menu = int(input())
    if op_menu == 1:
        print("☆☆☆☆☆☆☆☆☆☆☆☆☆ Titulo ☆☆☆☆☆☆☆☆☆☆☆☆☆\nPor favor, escolha uma opção abaixo:\n ")
        print("\t1- Cadastrar Título \n\t2- Descadastrar Título \n\t3- Carregar Títulos")
        print("\t4- Voltar \n\t\t Digite o número da sua opção: ", end="")
        OpcaoMenuTitulo(int(input()))
    elif op_menu == 2:
        print("☆☆☆☆☆☆☆☆☆☆☆☆☆ Votação ☆☆☆☆☆☆☆☆☆☆☆☆☆\nPor favor, escolha uma opção abaixo:\n ")
        print("\t1- Cadastrar Candidatos\n\t2- Nova Votação\n\t3- Adicionar Voto\n\t4- Gerar Votos Aleatórios")
        print("\t5- Resultado Parcial da Eleição\n\t6- Voltar\n\t0- Sair\n\t\t Digite o número da sua opção: ", end="")
        OpcaoMenuVotacao(int(input()))


def OpcaoMenuTitulo(entrada):  # Função que será chamada para exibir o menu dos títulos
    if entrada == 1:
        CadastrarTitulo()
    elif entrada == 2:
        DescadastrarTitulo()
    elif entrada == 3:
        CarregarTitulos()
    elif entrada == 4:
        Voltar()


def OpcaoMenuVotacao(entrada):  # Função que será chamada para exibir o menu de votação
    if entrada == 1:
        CadastrarCandidatos()
    elif entrada == 2:
        NovaVotacao()
    elif entrada == 3:
        AdicionarVoto()
    elif entrada == 4:
        GerarVotosAleatorios()
    elif entrada == 5:
        ResultadoParcial()
    elif entrada == 6:
        Voltar()
    elif entrada == 0:
        Sair()


def visualizarpre():
    arvore_de_eleitores.preorderVP(arvore_de_eleitores.getraiz())  # visualiza a arvore RB na Pré Ordem


def CadastrarTitulo():
    print("Por favor, digite o número do Titulo de Eleitor: ", end="")
    numero_titulo = int(input())
    if arvore_de_eleitores.procurarVP(
            numero_titulo) is None:  # Procura o titulo inserido na arvore de eleitores, caso o titulo nao seja encontrado
        arvore_de_eleitores.inserirVP(numero_titulo)  # o titulo é inserido na arvore de eleitores
        visualizarpre()
        print("\nTitulo Cadastrado")
        return Voltar()  # Volta ao menu principal após o titulo ter sido cadastrado automaticamente
    else:  # Caso o titulo ja tenha sido cadastrado, não insere o titulo  na arvore e exibe a mensagem
        print("\nErro! Titulo já cadastrado no sistema")
        return Voltar()


def DescadastrarTitulo():
    print("Por favor, digite o número do Título de Eleitor que deseja excluir: ", end="")
    numero_titulo = int(input())  # Recebe um titulo que sera removido do sistema
    if arvore_de_eleitores.procurarVP(numero_titulo):  # Procura o titulo digitado na arvore de eleitores
        arvore_de_eleitores.remover_rb(
            arvore_de_eleitores.procurarVP(numero_titulo))  # Se encontrar remove o titulo da arvore de eleitores
        visualizarpre()
        print()
        print("Título de eleitor descadastrado com sucesso!")
        Voltar()
    else:
        print(
            "\nErro! Título incorreto! 1- Tentar Novamente\t2- Voltar")  # Caso nao encontre o título digitado na arvore de eleitores significa que ele não existe
        n = int(input())
        if n == 1:
            DescadastrarTitulo()
        elif n == 2:
            Voltar()


def CarregarTitulos():
    print('Títulos: ')
    for i in range(100):  # Carrega automaticamente e aleatoriamente 100 titulos de eleitores
        x = randint(1000, 9999)
        if arvore_de_eleitores.procurarVP(x) is None:
            arvore_de_eleitores.inserirVP(x)  # preenche a arvore de eleitores
    arvore_de_eleitores.preorderVP(arvore_de_eleitores.getraiz())
    print()
    return Voltar()


def CarregarTitulosAleatorios():
    print('Títulos: ')
    for i in range(100):  # Carrega automaticamente e aleatoriamente 100 titulos de eleitores
        x = randint(1000, 9999)
        if arvore_de_eleitores.procurarVP(x) is None:
            arvore_de_eleitores.inserirVP(x)  # preenche a arvore de eleitores
    arvore_de_eleitores.preorderVP(arvore_de_eleitores.getraiz())
    print()


def CadastrarCandidatos():
    print("Por favor, digite o nome e número do candidato: ", end="")  # Recebe o nome e o numero do candidato
    entrada_candidato = input().split()
    if entrada_candidato not in todos_candidatos:  # se o candidato não está na lista todos_candidatos
        todos_candidatos.append(entrada_candidato)  # todos_candidatos adiciona a entrada do cadastramento na lista
        print("Candidato cadastrado com sucesso!")
        return Voltar()
    else:  # se estiver, não adiciona
        print("Esse candidato já foi cadastrado!")
    # pos 0 nome pos 1 número do cand


def VerificarTituloRB(titulo):
    if arvore_de_eleitores.procurarVP(titulo) is not None:  # tem o titulo procurado na ARB
        print("O titulo existe no sistema")
        return True
    else:
        print("O titulo não existe no sistema")
        return False


def VerificarTituloAB(titulo):
    if arvore_de_votacao.procurarAB(titulo) is not None:  # tem o titulo procurado na AB
        print("Esse titulo já realizou o voto")
        return True
    else:
        print("Esse titulo não realizou o voto")
        return False


def NovaVotacao():
    if arvore_de_votacao.ehVazio() is False:  # tem algo na arvore
        ResetArvoreVotacao()

    else:
        print("A Árvore está resetada")
    return Voltar()


def ResetArvoreVotacao():
    arvore_de_votacao = None
    return True


# Adicionar voto: ler número do título e o voto. Se o número do título é válido
# e se ainda não votou, contabiliza o voto e atualiza a árvore de votação
# que armazena os títulos de quem já votou;


def AdicionarVoto():
    global olhou
    olhou = False
    print("Digite o número do titulo e o voto: ", end="")
    titulo_voto = list(map(int, input().split()))
    if VerificarTituloRB(titulo_voto[0]) is True:  # titulo valido
        if VerificarTituloAB(titulo_voto[0]) is False:  # e n votou
            arvore_de_votacao.inserir(int(titulo_voto[0]))  # insere o titulo na arvore
            print("Voto computado com sucesso!")
            arvore_de_votacao.preorder(arvore_de_votacao.getraiz())
            voto.append(titulo_voto[1])  # lista com os votos
            return Voltar()

    else:
        print("Titulo invalido")


def ResultadoParcial():
    global candidato_qntVotos
    if olhou is False:  # inserindo candidado manualmente
        for i in voto:  # voto == todos os votos feitos
            if i not in candidato_sem_repeticao:  # se i não está nessa lista
                candidato_sem_repeticao.append(i)  # essa lista add apenas um numero por candidato
        for a in todos_candidatos:  # nessa lista a[0] = nome do candidato ; a[1] = numero do candidato
            for e in candidato_sem_repeticao:
                if int(a[
                           1]) == e:  # se o numero do candidato é igual a um elemento da lista que só tem um numero por candidato
                    x = a[0], voto.count(
                        e)  # nome do candidato , soma de todas as vezes que o elemento e aparece na lista de todos os votos realizados
                    candidato_qntVotos.append(x)
        print(candidato_qntVotos)
        ganhador = 0
        for i in range(len(candidato_qntVotos)):
            if candidato_qntVotos[i][1] > candidato_qntVotos[ganhador][1]:
                ganhador = i
        print('\nGanhador:', end='')
        print(candidato_qntVotos[ganhador])
        print()
        Voltar()
    else:  # olhou True inserindo votos aleatorios

        print("\nNúmero dos candidatos participantes: ", num_do_candidato_aleatorio)
        print("\nTodos os votos aleatórios: ", todos_votos_aleatorios)
        for a in num_do_candidato_aleatorio:
            x = a, todos_votos_aleatorios.count(a)
            candidato_qntVotos.append(x)

    print("\nNúmero do candidato / Total de votos")
    print(candidato_qntVotos)  # printa o candidato e a qnt de votos
    ganhador = 0
    for i in range(len(candidato_qntVotos)):
        if candidato_qntVotos[i][1] > candidato_qntVotos[ganhador][1]:
            ganhador = i
    print('\nGanhador:', end='')
    print(candidato_qntVotos[ganhador])
    print()
    Voltar()


def GerarVotosAleatorios():
    global olhou
    global todos_votos_aleatorios
    global num_do_candidato_aleatorio
    num_do_candidato_aleatorio, todos_votos_aleatorios = [], []
    CarregarTitulosAleatorios()
    for i in range(5):  # quantidade de candidatos
        x = randint(10, 99)
        if x not in num_do_candidato_aleatorio:
            num_do_candidato_aleatorio.append(x)
        else:
            num_do_candidato_aleatorio.append(x + 1)
    for a in range(100):
        y = random.choice(num_do_candidato_aleatorio)
        todos_votos_aleatorios.append(y)

        olhou = True
    print('Votos realizados:', end=' ')
    for i in range(len(todos_votos_aleatorios)):
        print(todos_votos_aleatorios[i], end=' ')
    print()
    Voltar()


def Sair():
    print("\nSistema de Eleição encerrado com sucesso.\n\t   ☆☆☆☆☆ Obrigado! ☆☆☆☆☆")
    arvore_de_eleitores = None
    arvore_de_votacao = None
    return True


def Voltar():
    IniciarMenu()


IniciarMenu()