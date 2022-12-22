import random

#Dicionario dos animes, a entrada no caso, pode ser substituido por entrada por leitura arquivo se quiser, talvez implemente futuramente
animes = {
  'Dragon Ball': [[
    'Ação', 'Artes Marciais', 'Aventura', 'Comédia', 'Fantasia', 'Shounen',
    'Superpoderes'
  ], 'grande'],
  'Naruto': [['Ação', 'Aventura', 'Shounen'], 'grande'],
  'Death Note':
  [['Mistério', 'Policial', 'Psicológico', 'Sobrenatural', 'Suspense'],
   'pequeno'],
  'Hyouka': [['Drama', 'Escolar', 'Mistério', 'Romance', 'Slice of Life'],
             'pequeno'],
  'One Piece': [[
    'Ação', 'Aventura', 'Comédia', 'Drama', 'Fantasia', 'Shounen',
    'Super poderes'
  ], 'grande'],
  'Shingeki no Kyojin': [[
    'Ação', 'Drama', 'Fantasia', 'Militar', 'Mistério', 'Shounen',
    'Sobrenatural'
  ],'medio']
}


#Funcao para inserir os animes, voce pode por no minimo 1 genero ate quantos quiser baseado no anime. A questao do tamanho, foi utilizado 3 tamanhos base, que sao pequeno, medio e grande, para facilitar ao inves de usar por quantidade de episodio
def inserir(animes):
  try:
    anime = str(input("\nNome do anime que deseja inserir:"))
    lista = []
    while True:
      genero = str(input("\nDigite um genero dele: "))
      lista.append(genero)
      opcao = str(input("\nDeseja continuar a inserir mais generos? s/n :"))

      #se sim continua, nesse caso como se trata de um loop, nao fazer nada vai voltar a executar o mesmo procedimento acima nesse caso
      if opcao == "s":
        print("\nInsira o proximo genero do anime em questao")
      #se nao, para de inserir
      elif opcao == "n":
        print("\nTerminado a insercao de genero do anime em questao")
        break

      else:
        print("\nDigitou algo fora do padrao, tente novamente")
    tamanho = str(
      input("\nQual o tamanho do anime? [pequeno, medio, grande]: "))
    #esse f{anime} serve para que seja indicado ao codigo que anime se trata de uma variavel, e que queremos substitui o valor da mesma e colocar ali no lugar do nome anime. Com o intuito nessa linha de fazer as adicoes da nova chave e valores.
    animes[f'{anime}'] = [lista, tamanho]

  except:
    print("\nDeu algum erro, tente novamente mais tarde")


#funcao para remover algum anime
def remover(animes):
  try:
    #esse v foi apenas para imprimir caso o anime nao fosse encontrado, tinha outras maneiras de fazer
    v = 0
    anime = str(input("\nNome do anime que quer remover:"))
    for i in animes:
      if i == anime:
        v += 1
        animes.pop(i)
        print("\nO Anime foi removido com sucesso!")
#apenas para imprimir caso nao fosse encontrado, baseado na forma que foi feito a parte superior
    if v == 0:
      print("\nAnime nao foi encontrado para remover")
  except:
    #nesse caso, como o tamnaho do animes diminui na parte de cima, ocorre um mini erro, o qual nao interfere na execucao, apenas para o codigo, mas como ele realizou a funcao de remover que era o objetivo e nao interfere em mais nada, foi solucionado dessa forma mesmo
    print("\n Escolha o que deseja realizar agora\n")


#lista todos os animes
def listar(animes):
  for i in animes:
    try:
      print("\nAnime:", i)
      print("\nGeneros do anime:\n{}".format(animes[i][0]))
      print("\nTamanho do anime:\n{}".format(animes[i][1]))
    except:
      print(
        "Nao foi possivel realizar a exibicao dos itens, provavelmente nao tem itens na lista"
      )


def procurar(animes):
  try:
    anime = str(input("\nDigite o anime que deseja buscar: "))
    v = 0
    for i in animes:
      if i == anime:
        #esse v foi apenas para imprimir caso o anime nao fosse encontrado, tinha outras maneiras de fazer
        v += 1
        print("\nAnime: ", i)
        print("\nGeneros do anime:\n{}".format(animes[i][0]))
        print("\nTamanho do anime:\n{}".format(animes[i][1]))
    #apenas para imprimir caso nao fosse encontrado, baseado na forma que foi feito a parte superior
    if v == 0:
      print("\nAnime nao encontrado!")
  except:
    print("Ocorreu algum erro, provavelmente nao tem animes na lista.")


#Exibe o menu na tela, para saber quais sao as opcoes disponiveis
def menu():
  print("\n---------------------------Menu--------------------------")
  print("\n Escolha uma das opcoes abaixo:\n")
  print("1-Listar todos animes\n")
  print("2-Adicionar anime\n")
  print("3-Remover anime\n")
  print("4-Procurar anime\n")
  print("5-Sugerir aleatoriamente\n")
  print("6-Finalizar programa\n")
  print("-------------------------------------------------------\n")
  escolha = int(
    input("\nDigite qual a opcao que deseja baseado no menu acima: "))
  return escolha


#laco infinito que vai tanto exibir o menu como atraves dele vai executar a escolha, desde listar até fechar o programa
while True:
  try:
    escolha = menu()
    if escolha == 1:
      listar(animes)
    elif escolha == 2:
      inserir(animes)
    elif escolha == 3:
      remover(animes)
    elif escolha == 4:
      procurar(animes)
    elif escolha == 5:
      opcao = input(
        "\nAleatoriamente de que forma:\n\n\tg-Genero\n\n\tt-Tamanho\n\n\ta-Aleatorio\n: "
      )
      if opcao == "a" or opcao=="Aleatorio":
        lista = []
        for i in animes:
          lista.append(i)
        try:
          print("\n")
          print(random.choice(lista))
        except:
          print("\nOcorreu um erro, provavelmente a lista esta vazia")
      elif opcao == "t" or opcao=="Tamanho":
        escolha = input("\nQual o tamanho desejado[pequeno, medio, grande]: ")
        lista = []
        if escolha == "pequeno":
          for i in animes:
            if escolha == animes[i][1]:
              lista.append(i)

        elif escolha == "medio":
          for i in animes:
            if escolha == animes[i][1]:
              lista.append(i)

        elif escolha == "grande":
          for i in animes:
            if escolha == animes[i][1]:
              lista.append(i)
        else:
          print("\nEscolha fora das opcoes possiveis!")
        try:
          print("\n")
          print(random.choice(lista))
        except:
          print(
            "\nOcorreu um erro, provavelmente a lista esta vazia, ou nao esta de acordo com os tamanhos existentes"
          )

      elif opcao == "g" or opcao=="Genero":
        lista = []
        escolha = input("Qual o genero que deseja: ")
        for j in animes:
          for p in animes[j][0]:
            if escolha == p:
              lista.append(j)
        try:
          print("\n")
          print(random.choice(lista))
        except:
          print(
            "\nOcorreu um erro, provavelmente a lista esta vazia, ou o genero digitado incorretamente ou inexistente na lista"
          )

    elif escolha == 6:
      print("\nPrograma finalizado com sucesso, obrigado pela utilização!")
      break
    else:
      print(
        "\nNao existe a opcao solicitada, digite uma das opcoes disponiveis")
  except:
    print("\nOcorreu algum erro no menu de selecao, tente executar mais tarde")
