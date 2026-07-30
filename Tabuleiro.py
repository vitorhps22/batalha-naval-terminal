import random

class Tabuleiro:
  def __init__(self,numLinhas,numColunas, numNavios, numSubmarinos):
    self.numLinhas = numLinhas
    self.numColunas = numColunas
    #
    self.tabuleiro = [0] * (self.numColunas * self.numLinhas)
    #
    self.numNavios = numNavios
    self.numSubmarinos = numSubmarinos
    #
    self.posicaoEmbarcacoes = {}
    self.indiceReversoPosicoesBarcos = {}
    #
    self.posicionarBarcos()

  def posicionarBarcos(self):
    #
    numNavios = 0
    while numNavios < self.numNavios:
      linhaTentativa  = random.choice(range(self.numLinhas))
      colunaTentativa = random.choice(range(self.numColunas))
      if self.getPosicao(linhaTentativa,colunaTentativa) == 0:
        self.setPosicao(linhaTentativa,colunaTentativa,1)
        nome = 'b' + str(numNavios) 
        #
        self.posicaoEmbarcacoes[nome] = {(linhaTentativa,colunaTentativa):1}
        self.indiceReversoPosicoesBarcos[(linhaTentativa,colunaTentativa)] = nome
        #
        numNavios += 1  
    
    #
    numSubmarinos = 0
    while numSubmarinos < self.numSubmarinos:
      linhaTentativa  = random.choice(range(self.numLinhas-1))
      colunaTentativa = random.choice(range(self.numColunas-1))
      if self.getPosicao(linhaTentativa,colunaTentativa) == 0 and self.getPosicao(linhaTentativa+1,colunaTentativa) == 0:
        self.setPosicao(linhaTentativa,colunaTentativa,1)
        self.setPosicao(linhaTentativa+1,colunaTentativa,1)
        #
        nome = 's' + str(numSubmarinos) 
        self.posicaoEmbarcacoes[nome] = {(linhaTentativa,colunaTentativa):1,
                                         (linhaTentativa+1,colunaTentativa):1}
        #
        self.indiceReversoPosicoesBarcos[(linhaTentativa,colunaTentativa)] = nome
        self.indiceReversoPosicoesBarcos[(linhaTentativa+1,colunaTentativa)] = nome
        #
        numSubmarinos += 1 
      elif self.getPosicao(linhaTentativa,colunaTentativa) == 0 and self.getPosicao(linhaTentativa,colunaTentativa+1) == 0:
        self.setPosicao(linhaTentativa,colunaTentativa,1)
        self.setPosicao(linhaTentativa,colunaTentativa+1,1)
        #
        nome = 's' + str(numSubmarinos) 
        self.posicaoEmbarcacoes[nome] = {(linhaTentativa,colunaTentativa):1,
                                         (linhaTentativa,colunaTentativa+1):1}
        #
        self.indiceReversoPosicoesBarcos[(linhaTentativa,colunaTentativa)] = nome
        self.indiceReversoPosicoesBarcos[(linhaTentativa,colunaTentativa+1)] = nome
        #
        numSubmarinos += 1


  def getDimensoes(self):
    return (self.numLinhas, self.numColunas)

  def getPosicao(self,i,j):
    return self.tabuleiro[i * self.numColunas + j]

  def setPosicao(self,i,j, valor):
    self.tabuleiro[i * self.numColunas + j] = valor

def teste():
  linhas  = 6
  colunas = 6 
  tabuleiro = Tabuleiro(linhas,colunas,3,2)
  revelar = True
  sep = '  '
  for i in range(linhas):
    for j in range(colunas):
      if revelar:
        print(str(tabuleiro.getPosicao(i,j)), end=sep)
      else:
        print('\u2588', end=sep)
    print()

