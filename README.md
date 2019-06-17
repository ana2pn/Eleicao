										Projeto: Eleições – Contagem e Checagem de Votos
1.Definição
	Nas nossas eleições é sabido que são utilizadas urnas eletrônicas. É desejado a construção de um
sistema que consiga contar os votos e checar quais os títulos que realizaram o processo de votação e
os que não votaram. Algumas medidas a serem tomadas são: verificar no momento que um
indivíduo vota se o título de eleitor dele é válido e, verificar também, se este eleitor ainda não
votou.

2.Estruturas de Dados e Detalhes de Implementação
	As verificações mencionadas na descrição acima devem ser feitas da seguinte forma: armazenar em
uma árvore vermelho-preta os números de todos os títulos válidos, chamada árvore de eleitores e
armazenar em outra árvore binária de busca os números de todos os títulos que já votaram até o
momento, chamada árvore de votação. O sistema é composto de duas partes: Cadastramento deTítulos de Eleitor e Votação.

2.1. O cadastramento de títulos de eleitor possuem as seguintes opções:
• Cadastrar título;

• Descadastrar título ;

• Carregar títulos;
    São números automaticamente para preencher a árvore.
	
2.2. A votação possui as seguintes opções:
• Cadastrar candidatos (nome e número);

• Nova votação: dá um “reset” na árvore de votação que guarda os títulos que já votaram.
Esse “reset” corresponde à liberação da memória dinamicamente alocada;

• Adicionar voto: ler número do título e o voto. Se o número do título é válido e se ainda
não votou, contabiliza o voto e atualiza a árvore de votação que armazena os títulos de
quem já votou;

• Gerar votos aleatórios (para encher a árvore de votação mais rapidamente): sempre
acionando a operação de inserir mais um elemento na árvore de votação;

• Apresentar o resultado parcial da eleição;

• Sair: destruir todas as estruturas e encerrar o programa.
