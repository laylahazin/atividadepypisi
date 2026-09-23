
#atividade pratica metodos de strings em python
#pisi I

print("====================================")
print("     MÉTODOS DE STRINGS EM PYTHON")
print("====================================")

print("1 - strip()")
print("2 - lower()")
print("3 - upper()")
print("4 - title()")
print("5 - replace()")
print("6 - split()")
print("7 - join()")
print("8 - count()")
print("9 - startswith()")
print("10 - endswith()")
print("11 - find()")
print("12 - isalpha()")
print("13 - isdigit()")
print("14 - isalnum()")
print("15 - isspace()")
print("16 - isupper()")
print("17 - islower()")
print("18 - zfill()")

escolha = input("Digite o número da questão que deseja executar: ")


#1-a) Leia o nome de um cliente com espaços antes exiba o nome sem esses espaços extras
nome=input("digite o nome do cliente").strip()
print(nome)
#1-b)Leia termo busca para catálogo e remova espaços extras das extremidades antes de pesquisar
termo=input("o que voce quer comer hoje?").strip()
print("Voce pesquisou por:",termo)

#2-a)Leia comando SAIR, Sair ou sair e converta minúsculas antes de verificar se o usuário deseja encerrar
while True:
    comando= input("Digite um comando SAIR para encerrar").strip()
    if comando.lower() == "sair": 
        print ("voce saiu da pagina")
        break

    else:
        print("Voce deseja permanecer na pagina?")

#2-b)Leia endereço e-mail e armazene uma versão em letras minúsculas para comparação
email=input("Digite seu endereço de e-mail:")
emailmin=email.lower()
print(f"o seu email é: {email} e seu email minusculo é:{emailmin}" )

#3-a)Leia código de um produto e converta-o para letras maiúsculas antes de exibi-lo
codigo=input("Digite o código do seu produto").upper()
print(codigo)

#3-b)Leia a sigla de um estado digitada pelo usuário e padronize-a em maiúsculas
estado=input("Qual o Estado que voce mora?").upper()
print(estado)

#4-a)Leia nome completo de uma pessoa e exiba-o com a primeira letra de cada palavra em maiúscula
nomemaiu=input("Qual o seu nome?").title()
print(nomemaiu)

#4-b) Leia o nome de um evento e apresente-o como título na tela inicial do programa
evento= input("Qual o evento que voce deseja ir?").title()
print(f"O evento que voce escolheu é o {evento}")

#5-a) Leia um telefone no formato 99999-9999 e remova o hífen antes de armazená-lo
telefone=input("Digite o número do seu telefone").replace('-', '')
print(f"confirme o seu num.: {telefone}")

#5-b) Leia um valor digitado como 19,90 e substitua a vírgula por ponto antes de convertê-lo para número
valor=input("Digite o valor").replace(",",".")
print(f"o valor do produto escolhido é: {valor}")

#6-a)Leia nome, idade e cidade em uma única linha separados por ponto e vírgula e separe os três campos
dados=input("Digite: Nome; idade; cidade").replace(" ","").split(";")
print (f"Confira seus dados: {dados}")

#6-b)Leia palavras-chave separadas por vírgulas e transforme a entrada em uma lista de termos
lista=input("Digite: Nome, idade, cidade ").replace(" ","").split(",")
print(f"Essa é sua lista de termos:{lista}")

#7-a) Dada uma lista com nomes de integrantes de uma equipe, exiba todos uma única linha separados vírgula
integrantes=input("Digite os integrantes da sua equipe").replace(" ","").split(",")
print(f"Essa é a sua equipe:{",".join(integrantes)}")

#7-b) Dada lista representando opções percorridas menu, exiba o caminho usando " > " como separador
opcoes = input("Digite as opções separadas por vírgula: ").replace(" ","").split(",")
tupla1 = tuple(opcoes)
tupla2 = " > ".join(tupla1)
print(tupla2)

#8-a)Leia uma frase curta e informe quantas vezes a letra "a" aparece nela
letraa=input("Escreva uma frase curta e vamos ver quantas vezes aparece a letra A").lower()
print("A quantidade de letras a é: ",letraa.count("a")) 

#8-b)Leia uma anotação e informe quantas vezes a palavra "erro" ocorre no texto
letraerro=input("Escreva uma frase curta e vamos ver quantas vezes aparece a palavra Erro").lower()
print("A quantidade de palavras erro é: ",letraerro.count("erro"))

#9-a) Leia um comando e verifique se ele começa com "/", indicando que é um comando especial
lercomando= input("Digite um comando: ")
print("O comando é especial?",lercomando.startswith("/")) 

#9-b) Leia um código de produto e verifique se ele começa com o prefixo "PROD-"
lercodigo= input("Digite o código do produto: ").lower().strip() 
print("O codigo começa com PROD-?",lercodigo.startswith("PROD-"))

#10-a) Leia o nome de um arquivo e verifique se ele termina com ".csv"
arquivo=("Digite o nome do arquivo: ")
print("O arquivo termina com .cvs?", arquivo.endswith(".cvs"))

#10-b) Leia um e-mail institucional e verifique se ele termina com "@ufrpe.br"
emailinst=input("Digite um email institucional: ")
print("Esse email é institucional?", emailinst.endswith("@ufrpe.br"))

#11-a) Leia um e-mail e informe a posição em que o caractere "@" aparece
leremail=input("Digite o seu email para verificação: ")
print("A posição do @ é:", leremail.find("@"))

#11-b) Leia uma entrada no formato comando:valor e informe a posição do caractere ":"
entrada= input("Digite uma entrada no formato comando valor: ")
print("A posição é: ", entrada.find(":"))

#12-a) Leia um primeiro nome e verifique se ele contém apenas letras
lerletras=input("Digite seu primeiro nome: ")
print("Seu primeiro nome contém apenas letras? ", lerletras.isalpha() )

#12-b) Leia uma categoria curta, como livros ou jogos, e valide se foram digitadas apenas letras
lercategoria=input("Escolha uma categoria entre Livros ou jogos: ")
print("A categoria escolhida contém apenas letras?", lercategoria.isalpha())

#13-a) Leia a opção escolhida em um menu e verifique se a entrada contém apenas dígitos antes de convertê-la para inteiro
lerdigitos=input("Escolha uma das seguintes opções: 1,2,3,4 ou 5 ")
print("A opção escolhida contém apenas números?", lerdigitos.isdigit())

#13-b) Leia a idade informada pelo usuário e valide se foram digitados apenas números
leridade=input("Digite a sua idade: ")
print("A idade contém apenas números?", leridade.isdigit())

#14-a) Leia um código de acesso e verifique se ele contém somente letras e números, sem símbolos ou espaços
lercodigo=input("Digite seu código de acesso: ")
print("O código contém apenas letras e números? ", lercodigo.isalnum())

#14-b) Leia um identificador simples de produto e aceite-o somente se for alfanumérico
identificador=input("Digite o identificador do produto: ")
print("O identificador do produto contém apenas letras e números? ", identificador.isalnum())

#15-a) Leia um campo de observação e verifique se o usuário digitou apenas espaços em branco
observacao=input("Digite espaços em branco: ")
print("O campo contém apenas espaços em branco?", observacao.isspace())

#15-b) Leia uma resposta e detecte se ela contém somente espaços ou tabulações, tratando-a como vazia
lerresposta=input("Esse campo deve conter apenas espaços ou tabulações: ")
print("Essa resposta está vazia?", lerresposta.isspace())

#16-a) Leia uma sigla e verifique se todas as letras foram digitadas em maiúsculas
sigla=input("Digite uma sigla:")
print("A sigla está em letras maiúsculas? ", sigla.isupper())

#16-b) Leia um código de categoria que deve estar em maiúsculas e informe se o formato está correto
categoriamaiu=input("Digite o código da categoria em letras maiúsculas: ")
print("O código da categoria está em correto?", categoriamaiu.isupper())

#17-a) Leia um comando que deve ser digitado em minúsculas e valide o formato antes de executá-lo
comandomin=input("Digite um comando em letras minúsculas: ")
print("O comando está em letras minúsculas? ", comandomin.islower())

#17-b) Leia um nome de usuário simples e verifique se todas as letras estão em minúsculas
lerusuariomin=input("Digite seu nome de usuário: ")
print("O nome de usuário está em letras minúsculas?", lerusuariomin.islower())

#18-a) Leia o número de uma senha de atendimento e exiba-o sempre com 5 dígitos, completando com zeros à esquerda
senha=input("Digite o numero da senha de atendimento: ")
print("Senha de atendimento: ", senha.zfill(5))

#18-b) Leia o número de uma nota ou pedido e exiba-o com 8 posições, usando zeros à esquerda quando necessário
npedido=input("Digite o numero da nota ou pedido: ")
print("Nota ou pedido número:", npedido.zfill(8))
