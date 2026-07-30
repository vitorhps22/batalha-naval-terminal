# caracteres utilizados
# caracteres utilizados
def mostrarCaracteresUsados():
    print('O caractere: _  é usado para água 💦')
    print('O caractere: N  é usado para navio acertado 💥')
    print('O caractere: S  é usado para submarino acertado 💥')
    print('O caractere: □  é usado para representar coordenadas ainda não reveladas no jogo ❓')

def escolher_simbolo(tabuleiro, i, j, revelar):
    valor = tabuleiro.getPosicao(i, j)
    
    if valor == 9:  # Acerto em navio/submarino
        nome_barco = tabuleiro.indiceReversoPosicoesBarcos.get((i, j), "")
        if nome_barco.startswith("b"):
            return "N"
        elif nome_barco.startswith("s"):
            return "S"
        else:
            return "✖︎"
    elif valor == 8:  # Água (erro)
        return "_"
    elif revelar and valor == 1:  # Navio não descoberto (só mostra se revelar=True)
        return "N"
    else:  # Coordenada não revelada
        return "□"

def imprimir_tabuleiro(tabuleiro, revelar=False):
    linhas, colunas = tabuleiro.getDimensoes()
    # ^ centraliza o texto em um campo de 3 espaços
    #numeros das colunas
    print("    ", end="")
    for j in range(colunas):
        print(f"{j:^3}", end="")
    print()

    #letras das linhas
    for i in range(linhas):
        letra = chr(ord("A") + i)
        print(f"{letra} | ", end="")

        for j in range(colunas):
            simbolo = escolher_simbolo(tabuleiro, i, j, revelar)
            print(f"{simbolo:^3}", end="")
        print()
        