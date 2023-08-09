import pandas as pd
import numpy as np
import statistics
from tabulate import tabulate

def saudacoes():
  print('=' * 136)
  print('''Olá, docente! Seja bem-vindo à calculadora de estatísticas de notas escolares

Antes de começar a utilizar as funções e realizar cálculos, primeiro insira as informações de sua turma, por favor:''')
  print('=' * 136)
  print()

def cadastra_informacoes_turma():
  numero_alunos = input("Quantos alunos a sua turma tem? ")
  while not numero_alunos.isdigit() or int(numero_alunos) <= 1 or int(numero_alunos) > 90:
    print("\nInsira um número válido, sabendo que uma turma tem entre dois e 90 alunos.")
    numero_alunos = input("Quantos alunos a sua turma tem? ")
  numero_alunos = int(numero_alunos)

  numero_provas = input("O método avaliativo consiste na realização de quantas provas por período? ")
  while not str(numero_provas).isdigit() or int(numero_provas) < 1:
    print("\nInsira um número válido, sabendo que o número mínimo de provas que uma turma deve ter é 1.")
    numero_provas = input("O método avaliativo consiste na realização de quantas provas por período? ")
  numero_provas = int(numero_provas)

  aulas_ministradas = input("Quantas aulas foram ministradas durante o quadrimestre? ")
  while not aulas_ministradas.isdigit() or int(aulas_ministradas) < 1 or int(aulas_ministradas) > 12:
    print("\nInsira um número válido (entre 1 e 12).")
    aulas_ministradas = input("Quantas aulas foram ministradas durante o quadrimestre? ")
  aulas_ministradas = int(aulas_ministradas)

  recuperacao_aberta = input("\nA recuperação da disciplina é aberta aos estudantes? (sim/nao) ").lower()
  while recuperacao_aberta not in ("sim", "nao"):
    recuperacao_aberta = input("Digite uma palavra válida, sim ou nao: ")
    print()

  return numero_alunos, numero_provas, aulas_ministradas, recuperacao_aberta

def cadastra_notas_frequencias(numero_alunos, numero_provas, aulas_ministradas):
  '''
  Função que permite cadastrar as notas e frequências de um aluno
  '''
  alunos_notas = []
  alunos_frequencias = []
  for aluno_num in range(numero_alunos):
    print(f"\nDigite as notas das provas e aulas assistidas do aluno {aluno_num + 1} nas linhas a seguir.")
    notas = []
    for prova_num in range(numero_provas):
        nota = input(f"Nota da P{prova_num + 1}: ")
        if "," in nota:
          nota = nota.replace(",", ".")
        while not nota.replace('.', '').isdigit() or float(nota) < 0 or float(nota) > 10:
          print("A nota de uma prova deve ser um NÚMERO entre 0 e 10, ambos inclusive.")
          nota = input(f"Nota da P{prova_num + 1}: ")
        nota = float(nota)
        nota = f'{nota:.2f}'
        nota = float(nota)
        notas.append(nota)

    # Nestas linhas, cadastramos a frequência (em %) de um determinado aluno nas aulas
    presenca = input(f"Quantas aulas o aluno {aluno_num + 1} assistiu? ")
    while not presenca.isdigit() or int(presenca) < 0 or int(presenca) > aulas_ministradas:
      print('''Um aluno pode assistir no mínimo zero aulas e, no máximo, todas as aulas que foram ministradas.
Além disso, a quantidade de aulas assistidas deve ser um número inteiro.''')
      presenca = input(f"Quantas aulas o aluno {aluno_num + 1} assistiu? ")
    presenca = int(presenca)
    frequencia = (presenca / aulas_ministradas) * 100
    frequencia = f'{frequencia:.2f}'
    frequencia = float(frequencia)

    alunos_frequencias.append(frequencia)            # ----> "alunos_frequencias" é um vetor
    alunos_notas.append(notas.copy())                # ----> "alunos_notas" é uma matriz
  return alunos_notas, alunos_frequencias

# é necessário criar uma cópia das linhas da matriz
# para garantir que cada linha seja uma lista diferente,
# evitando, assim, o problema de todas as linhas serem iguais.

def verifica_conceito(numero):
  if 8.5 <= numero <= 10:
    conceito = "A"
  elif 7.0 <= numero < 8.5:
    conceito = "B"
  elif 6.0 <= numero < 7.0:
    conceito = "C"
  elif 4.5 <= numero < 6.0:
    conceito = "D"
  elif numero < 4.5:
    conceito = "F"
  return conceito

def verifica_aprovado_ou_reprovado(conceito):
  if conceito == "A" or conceito == "B" or conceito == "C" or conceito == "D":
    aprovado_ou_reprovado = "aprovado"
  else:
    aprovado_ou_reprovado = "reprovado"
  return aprovado_ou_reprovado

def verifica_necessidade_recuperacao(recuperacao_aberta, conceito):
  if conceito == "A" or conceito == "B":
    necessidade_recuperacao = "não terá direito à recuperação"
  elif recuperacao_aberta == "sim" and conceito == "C" or conceito == "D":
    necessidade_recuperacao = "terá direito à recuperação"
  elif recuperacao_aberta == "nao" and conceito == "D":
    necessidade_recuperacao = "terá direito à recuperação"
  elif recuperacao_aberta == "nao" and conceito == "C":
    necessidade_recuperacao = "não terá direito à recuperação"
  elif conceito == "F":
    necessidade_recuperacao = "deverá fazer a recuperação obrigatoriamente, senão reprovará"
  return necessidade_recuperacao

def mostra_matriz_ou_vetor(matriz_ou_vetor):
  '''
  Função que mostra uma matriz ou vetor qualquer, sendo que
  o parâmetro desta função é a matriz ou o vetor a ser mostrada (o).
  '''
  for indice in range(len(matriz_ou_vetor)):    # a função len(notas) retorna o número de linhas da matriz
    print("Aluno " + str(indice + 1) + ":", matriz_ou_vetor[indice])
  print()

def consulta_provas_aluno(matriz_notas, indice_aluno):
  numero_provas = len(matriz_notas[0])
  for indice_prova in range(numero_provas):
    nota = matriz_notas[indice_aluno - 1][indice_prova]
    conceito = verifica_conceito(nota)
    print(f"A nota da P{indice_prova + 1} do aluno {indice_aluno} é {nota}, equivalente ao conceito {conceito}.")

def consulta_media_individual(matriz_notas, indice_aluno):
  numero_provas = len(matriz_notas[0])
  for indice_prova in range(numero_provas):
    nota = matriz_notas[indice_aluno - 1][indice_prova]
    conceito = verifica_conceito(nota)
    print(f"A nota da P{indice_prova + 1} do aluno {indice_aluno} é {nota}, equivalente ao conceito {conceito}.")
  media = sum(matriz_notas[indice_aluno - 1]) / len(matriz_notas[indice_aluno - 1])
  return media

def medias_individuais(matriz_notas, recuperacao_aberta):
  numero_alunos = len(matriz_notas)
  for indice_aluno in range(numero_alunos):
    media = sum(matriz_notas[indice_aluno]) / len(matriz_notas[indice_aluno])
    conceito = verifica_conceito(media)
    necessidade_recuperacao = verifica_necessidade_recuperacao(recuperacao_aberta, conceito)
    aprovado_ou_reprovado = verifica_aprovado_ou_reprovado(conceito)
    print(f"A média final do aluno {indice_aluno + 1} é {media}, equivalente ao conceito {conceito}. Portanto, o aluno foi, em tese, {aprovado_ou_reprovado}.")
    print(f"E, por obter um conceito final {conceito}, este aluno {necessidade_recuperacao}.")

def medias_provas(matriz_notas):
  numero_provas = len(matriz_notas[0])
  soma = 0
  for indice_prova in range(numero_provas):
    for notas_aluno in matriz_notas:
      soma += notas_aluno[indice_prova]
    media = soma / len(matriz_notas)
    conceito = verifica_conceito(media)
    soma = 0
    print(f"A média da P{indice_prova + 1} é {media}, equivalente ao conceito {conceito}.")

def calcula_media_turma(matriz_notas):
  soma = 0
  elementos = [elemento for linha in matriz_notas for elemento in linha]
  for valor in elementos:
    soma += valor
  media = soma / len(elementos)
  media = float(f'{media:.2f}')
  return media

def calcula_mediana(lista):
    lista_ordenada = sorted(lista)  # a função sorted transforma seu parâmetro (lista) em uma nova lista, que é ordenada
    numero_elementos = len(lista_ordenada)
    if numero_elementos % 2 == 0:
        # Se o número de elementos for par, a mediana é a média dos dois valores centrais
        meio1 = lista_ordenada[numero_elementos // 2 - 1]
        meio2 = lista_ordenada[numero_elementos // 2]
        mediana = (meio1 + meio2) / 2
    else:
        # Se o número de elementos for ímpar, a mediana é o valor central
        mediana = lista_ordenada[numero_elementos // 2]
    return mediana

def calcula_medianas_provas(alunos_notas):
    numero_provas = len(alunos_notas[0])
    medianas_provas = []

    for prova in range(numero_provas):
        notas_prova = [aluno[prova] for aluno in alunos_notas]
        mediana_prova = calcula_mediana(notas_prova)
        medianas_provas.append(mediana_prova)
    return medianas_provas

def calcula_moda_matriz(matriz):
    elementos = [elemento for linha in matriz for elemento in linha]
    moda = statistics.multimode(elementos)
    moda = ', '.join(str(moda) for moda in moda)     # A função join só funciona para strings, portanto, temos que percorrer
                                                     # os elementos da lista de modas, um por um, e transformá-los em strings.
    return moda

def desvio_padrao_medias_individuais(matriz_notas):
  '''
  Esta função calcula o desvio padrão das médias individuais em relação
  à média final da turma
  '''

  #Função que calcula a média de todos os elementos da matriz mas nós iremos importar o resultado da função média
  media_turma = calcula_media_turma(matriz_notas)

  #Calcula a média de cada linha
  medias_individuais = np.mean(matriz_notas, axis=1)

  #Função que calcula o desvio padrão das médias individuais em relação à média final da turma
  desvio_padrao_medias = np.std(medias_individuais - media_turma)

  return desvio_padrao_medias

def tabela(alunos_notas, alunos_frequencias):
    colunas_provas = [f"P{i + 1}" for i in range(len(alunos_notas[0]))]
    data = {"Frequência (%)": alunos_frequencias}
    df = pd.DataFrame(data)

    # Adiciona colunas representando cada prova
    for i, coluna_prova in enumerate(colunas_provas):
        df[coluna_prova] = [notas[i] for notas in alunos_notas]

    # Remove o índice numérico
    df.index = ["Aluno " + str(i + 1) for i in range(len(alunos_notas))]

    # Mover coluna de frequência para a última posição
    cols = list(df.columns)
    cols.remove("Frequência (%)")
    df = df[cols + ["Frequência (%)"]]

    # Exibe a tabela formatada com divisões
    print(tabulate(df, headers='keys', tablefmt='grid'))

def calculadora_estatisticas_notas_escolares():  # Essa função é a principal "main()"
  '''
  O programa inicia com uma mensagem de cumprimento ao usuário,
  e em seguida solicita a inserção de informações da turma escolar (número de alunos e provas por semestre).

  Após isso, é mostrado um menu com uma série de opções disponíveis para o usuário,
  as quais realizarão diferentes funções estatísticas.

  Observações do menu interativo:

  1. O desvio padrão calculado utiliza como valores médios: a média geral da turma
  e as médias de cada avaliação;

  2. A moda calculada dá como resultado a nota que mais se repetiu na matriz de notas;

  3. Todas as médias são aritméticas, ou seja, são calculadas considerando
  que o peso das provas é igualmente distribuído.
  '''
  saudacoes()
  numero_alunos, numero_provas, aulas_ministradas, recuperacao_aberta = cadastra_informacoes_turma()

  print('\nAgora insira as notas e frequências de todos os alunos, em ordem numérica:')
  alunos_notas, alunos_frequencias = cadastra_notas_frequencias(numero_alunos, numero_provas, aulas_ministradas)

  volta_menu = "sim"
  while volta_menu == "sim":
    print()
    print("Agora, selecione uma função do menu:")
    opcao = input('''
------------------ FUNÇÕES ------------------

  1. Obter as médias aritméticas individuais, das provas e da turma

  2. Obter a mediana das provas e da turma

  3. Obter a moda das notas

  4. Obter o desvio padrão das médias individuais (em relação à média da turma)

  5. Consultar a média de um aluno específico

  6. Consultar as notas das provas de um aluno específico

  7. Visualizar as notas e frequências individuais em formato de matriz

  8. Visualizar as notas e frequências individuais em formato de tabela

  Escolha uma opção: ''')
    while not opcao.isdigit() or int(opcao) < 1 or int(opcao) > 8:  #Enquanto a opção for uma letra OU se a opção for um número menor que 1 OU maior que 7
      print()
      print("Selecione uma opção válida (de 1 a 6).")
      print()
      opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print()
      print('-' * 110)
      medias_individuais(alunos_notas, recuperacao_aberta)
      print()
      print('-' * 110)
      medias_provas(alunos_notas)
      print()
      print('-' * 110)
      media_turma = calcula_media_turma(alunos_notas)
      conceito = verifica_conceito(media_turma)
      print(f"A média da turma é {media_turma}, equivalente ao conceito {conceito}.\n")

    elif opcao == "2":
      lista_notas = [nota for aluno in alunos_notas for nota in aluno]  # lista com todas as notas (de todas as provas)
      mediana_turma = calcula_mediana(lista_notas)
      conceito = verifica_conceito(mediana_turma)
      aprovado_ou_reprovado = verifica_aprovado_ou_reprovado(conceito)
      print(f"\nA mediana geral da turma é: {mediana_turma:.2f}, equivalente ao conceito {conceito} ({aprovado_ou_reprovado}).")

      medianas_provas = calcula_medianas_provas(alunos_notas)
      print("\nAs medianas das notas de cada prova, por sua vez, são:\n")
      for prova, mediana in enumerate(medianas_provas, start = 1):  # este comando "start" define o valor inicial para a contagem dos índices do loop
        conceito = verifica_conceito(mediana)
        aprovado_ou_reprovado = verifica_aprovado_ou_reprovado(conceito)
        print(f"Mediana da prova {prova}: {mediana:.2f}, equivalente ao conceito {conceito} ({aprovado_ou_reprovado}).")
      print()

    elif opcao == "3":
      moda = calcula_moda_matriz(alunos_notas)
      print(f"O(s) valor(es) da moda na matriz de notas é(são): {moda}.")

    elif opcao == "4":
      desvio_padrao = desvio_padrao_medias_individuais(alunos_notas)
      print(f"O desvio padrão das médias individuais em relação à média da turma é: {desvio_padrao:.2f}")

    elif opcao == "5":
      numero_aluno = input("\nPor favor, digite o número do aluno que você deseja consultar a média: ")
      while not int(numero_aluno) in range(1, numero_alunos + 1) or not numero_aluno.isdigit():
        numero_aluno = input("\nDigite um número válido: ")
      numero_aluno = int(numero_aluno)
      media = consulta_media_individual(alunos_notas, numero_aluno)
      conceito = verifica_conceito(media)
      necessidade_recuperacao = verifica_necessidade_recuperacao(recuperacao_aberta, conceito)
      aprovado_ou_reprovado = verifica_aprovado_ou_reprovado(conceito)
      print(f"\nA média final do aluno {numero_aluno} é {media}, equivalente ao conceito {conceito}. Portanto, o aluno foi {aprovado_ou_reprovado}.")
      print(f"E, por obter um conceito final {conceito}, este aluno {necessidade_recuperacao}.")

    elif opcao == "6":
      numero_aluno = input("Por favor, digite o número do aluno que você deseja consultar as notas: ")
      while not int(numero_aluno) in range(1, numero_alunos + 1) or not numero_aluno.isdigit():
        numero_aluno = input("Digite um número válido.")
      numero_aluno = int(numero_aluno)
      consulta_provas_aluno(alunos_notas, numero_aluno)

    elif opcao == "7":
      print()
      print("-" * 18 + " NOTAS " + "-" * 18)
      mostra_matriz_ou_vetor(alunos_notas)
      print("-" * 18 + " FREQUÊNCIAS " + "-" * 18)
      mostra_matriz_ou_vetor(alunos_frequencias)

    elif opcao == "8":
      tabela(alunos_notas, alunos_frequencias)
      print()

    volta_menu = input("\nDeseja retornar ao menu principal? (sim/nao) ").lower()
    print()
    while volta_menu not in ("sim", "nao"):
      volta_menu = input("Digite uma palavra válida, sim ou nao: ")
      print()

calculadora_estatisticas_notas_escolares()
