#ADICIONANDO A BIBLIOTECA MATPLOTLIB.PYPLOT
import matplotlib.pyplot as plt
import numpy as np

#CRIANDO A CLASSSE PARA REPRESENTAR UM LIVRO
class Livro:#CONSTRUTOR DA CLASSE
    def __init__(self, titulo, autor, ano_publicacao, genero, quantidade): #INICIALIZANDO OS ATRIBUTOS
        self.titulo = titulo #TÍTULO DO LIVRO
        self.autor = autor #AUTOR DO LIVRO
        self.ano_publicacao = ano_publicacao #ANO DE PUBLICAÇÃO
        self.genero = genero #GENERO DO LIVRO
        self.quantidade = quantidade #QUANTIDADE DE EXEMPLARES DO LIVRO
    #METODO PARA REPRESENTAR O LIVRO COMO UMA STRING
    def __str__(self): #RETORNANDO UMA STRING COM AS INFORMAÇÕES DO LIVRO
        return f"Gênero do livro: {self.genero}, Título: {self.titulo}, Autor: {self.autor} ({self.ano_publicacao}), Quantidade: {self.quantidade}"
    
#CRIANDO UMA LISTA DE LIVROS
biblioteca = []

#LISTA PARA ARMAZENAR OS ANOS DE PUBLICAÇÃO
anos = []

generos =[] #LISTA PARA ARMAZENAR OS GENEROS

#FUNÇÃO PARA ADICIONAR UM LIVRO À BIBLIOTECA
def adicionar_livro(titulo, autor, ano_publicacao, genero, quantidade):
    novo_livro = Livro(titulo, autor, ano_publicacao, genero, quantidade)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao)
    generos.append(genero)
    print(f'Livro "{titulo}" adicionado à biblioteca.')

#FUNCAO PARA LISTAR TODOS OS LIVROS NA BIBLIOTECA
def listar_livros():
    if not biblioteca:
        print("A biblioteca está vazia.")
    else:
        print("\nLivros na biblioteca:")
        for livro in biblioteca:
            print(livro)
        print (64 * "=") #LINHA PARA SEPARAR OS LIVROS
        input("Pressione Enter para voltar para o menu...") #PAUSA PARA O USUÁRIO VOLTAR AO MENU
        print("\n") #LINHA EM BRANCO APÓS LISTAR OS LIVROS

#FUNÇÃO PARA EXIBIR GRÁFICO DE LIVROS POR GÊNERO
def mostrar_grafico():
     #GERANDO UM GRÁFICO DE LIVROS POR GÊNERO
    generos_unicos = sorted(set(generos))  # GÊNERO ÚNICO E ORDENADO

    #CONTANDO LIVROS POR GÊNERO
    contagem_por_generos = [generos.count(genero) for genero in generos_unicos] #CONTANDOA QUANTIDADE DE LIVROS POR GENERO

    #CRIANDO O GRÁFICO
    plt.plot(generos_unicos, contagem_por_generos, marker='o', linestyle='-') #PLOTANDO OS PONTOS E LINHAS
    plt.title('Número de Livros por Gênero de Publicação') #TÍTULO DO GRAFICO
    plt.xlabel('Gênero de Publicação') #LABEL DO EIXO X
    plt.ylabel('Número de Livros') #LABEL DO EIXO Y

    #ADICIONAR RÓTULO AOS PONTOS DE DADOS
    for i,valor in enumerate(contagem_por_generos):
        plt.text(generos_unicos[i], valor, str(valor), ha='center', va='bottom')

    plt.grid(True) #ADICIONANDO GRADE
    plt.show() #MOSTRANDO O GRÁFICO

#FUNÇÃO PARA INCLUIR NOVOS QUE FORAM DIGITADOS PELO USUÁRIO
def incluir_novos_livros():
    print("Adicione livros à sua biblioteca. Digite 'sair' como título para encerrar.\n")
    while True:
        titulo = input("Digite o título do livro (ou 'sair' para encerrar): ")
        if titulo.lower() == 'sair':
            break
        autor = str(input("Digite o autor do livro: "))
        ano_publicacao = int(input("Digite o ano de publicação do livro: "))
        genero = str(input("Digite o gênero do livro: "))
        quantidade = int(input("Digite a quantidade de exemplares do livro: "))
        adicionar_livro(titulo, autor, ano_publicacao, genero, quantidade)

#ADICONANDO LIVROS PARA JÁ COMECAR COM ALGUS LIVROS
#CRIANDO UMA LISTA COM LIVROS INICIAIS
livros_iniciais = [ #TÍTULO, AUTOR, ANO
    ("Codido da Vinci", "Dan Brown", 2003 ,"Ficção", 5),
    ("O simbolo perdido", "Dan Brown", 2009 ,"Ficção" , 3),
    ("Verity", "Colleen Hoover", 2018, "Romance", 4),
    ("A biblioteca da meia-noite", "Matt Haig", 2020, "Ficção", 2),
    ("A hipotese do amor", "Ali Hazelwood", 2021, "Romance", 6),
    ("It - A Coisa", "Stephen King", 1986, "Terror", 7),
    ("O iluminado", "Stephen King", 1977, "Terror", 5),
    ("Layla", "Colleen Hoover", 2020, "Romance", 4),
    ("Napoleão", "João C. Saldanha", 2017, "Biografia", 3),
    ("Martin lutero", "João C. Saldanha", 2017, "Biografia", 2),
    ("O pequeno príncipe", "Antoine de Saint-Exupéry", 1943, "Ficção", 8),
    ("Dom Quixote", "Miguel de Cervantes", 1605, "Ficção", 4),
    ("O senhor dos anéis", "J.R.R. Tolkien", 1954, "Ficção", 6),
    ("Python para desenvolvedores", "Wesley J. Chun", 2009, "Tecnologia", 5),
    ("Aprendendo Python", "Mark Lutz", 2013 ,"Tecnologia", 3),
    ("Automatize tarefas maçantes com Python", "Al Sweigart", 2015, "Tecnologia", 4),
    ("Fluent Python", "Luciano Ramalho", 2015, "Tecnologia", 2),
    ("PHP e MySQL", "Luke Welling e Laura Thomson", 2005, "Tecnologia", 6),
    ("JavaScript: The Good Parts", "Douglas Crockford", 2008, "Tecnologia", 4),
    ("Aprenda JavaScript", "Eloy Morais", 2017, "Tecnologia", 3),
    ("Domine o css", "Eloy Morais", 2017, "Tecnologia", 5),
    ("HTML5 e CSS3", "Eloy Morais", 2017, "Tecnologia", 4),
    ("PHP para iniciantes", "Eloy Morais", 2017, "Tecnologia", 2),
]
#ADICIONANDO OS LIVROS INICIAIS USANDO A FUNÇÃO
for titulo, autor, ano, genero, quantidade in livros_iniciais:
    adicionar_livro(titulo, autor, ano, genero, quantidade)
#FIM DAS ADICOES INICIAIS

#FUNCÃO PARA BUSCAR LIVROS PELO TÍTULO
def buscar_livro(titulo):
    resultados = [livro for livro in biblioteca if titulo.lower() in livro.titulo.lower()] #BUSCA INSENSÍVEL A MAIÚSCULAS E MINÚSCULAS
    if resultados: #VERIFICA SE HOUVE RESULTADOS
        print("Livros encontrados:")
        for livro in resultados:
            print(livro)
        print (64 * "=") #LINHA PARA SEPARAR OS LIVROS
        input("Pressione Enter para voltar para o menu...") #PAUSA PARA O USUÁRIO VOLTAR AO MENU
        print("\n") #LINHA EM BRANCO APÓS LISTAR OS LIVROS
    else:
        print("Nenhum livro encontrado com esse título.")


#ADICIONANDO USANDO WHILE
print("Bem-vindo à Biblioteca!\n")

#CRIANDO O MENU INICIAL
def inicio():
    while True:
        print("\nMenu Principal:")
        print(64 * "=") #LINHA PARA SEPARAR O MENU
        #MOSTRANDO AS OPÇÕES
        print("(0) Sair")
        print("(1) Adicionar um livro")
        print("(2) Listar livros")
        print("(3) Buscar um livro")
        print("(4) Para ver Número de Livros por Gêneros de Publicação")
        print(64 * "=") #LINHA PARA SEPARAR O MENU
        #PEGANDO A OPÇÃO ESCOLHIDA
        opcao = input("Digite 0, 1, 2, 3 ou 4: ")
        print("\n") #LINHA EM BRANCO APÓS PEGAR A OPÇÃO
        #VERIFICANDO A OPÇÃO ESCOLHIDA
        if opcao == '4': #EXIBE O GRAFICO
            mostrar_grafico()

        elif opcao == '3': #BUSCANDO LIVROS
            titulo_busca = input("Digite o título do livro que você quer buscar: ")
            buscar_livro(titulo_busca)

        elif opcao == '2': #LISTANDO LIVROS
            listar_livros()

        elif opcao == '1':#ADICIONANDO LIVROS
            incluir_novos_livros()
        elif opcao == '0': #SAINDO DO PROGRAMA
            break
        else:#OPÇÃO INVÁLIDA
            print("Opção inválida. Tente novamente.")
            
#CHAMANDO A FUNÇÃO INICIO
inicio()

print("\nObrigado por usar a Biblioteca!")
#FIM DO PROGRAMA
#CLICK EM ENTER PARA SAIR
input("Pressione Enter para sair...")
