from Tabuleiro import Tabuleiro
from Exibicao import imprimir_tabuleiro, mostrarCaracteresUsados
from Persistencia import salvar_pontuacao, mostrar_ranking
from time import sleep
# funções auxiliares
def ler_coordenada(entrada_do_jogador):
    entrada_do_jogador = entrada_do_jogador.strip().upper()
    if len(entrada_do_jogador) < 2:
        return None
    linha = ord(entrada_do_jogador[0]) - ord("A")
    try:
        coluna = int(entrada_do_jogador[1:])
    except ValueError:
        return None
    return linha, coluna
#contador de afundados
def contar_afundados(posicaoEmbarcacoes):
    navios = submarinos = 0
    for nome, partes in posicaoEmbarcacoes.items():
        if all(status == 0 for status in partes.values()):
            if nome.startswith("b"):
                navios += 1
            elif nome.startswith("s"):
                submarinos += 1
    return navios, submarinos

def tutorial ():
    print("\n📘 TUTORIAL - Batalha Naval")
    print("-" * 70)
    print("🎯 Objetivo:")
    print("Afundar todos os navios e submarinos do tabuleiro inimigo.")
    print()
    print("Como jogar:")
    print("O tabuleiro tem 6 linhas (A-F) e 6 colunas (0-5).")
    print("Você escolhe uma coordenada para atacar, por exemplo: B3 ou E0.")
    print("O jogo indica se você acertou ou errou.")
    print()
    print("condição de vitória:")
    print("Você vence quando todos os navios (N) e submarinos (S) forem afundados.")
    print()
    print("Dicas 💡:")
    print("Explore o tabuleiro de forma estratégica, tente descobrir o padrão.")
    print("Use as marcações do tabuleiro para evitar fazer jogadas repetidas.")
    print("Submarinos ocupam 2 coordenadas,já os navios ocupam apenas 1.")
    print()
    print("Boa sorte, comandante !!!\n")


class Jogo:
    #configurações do jogo
    def __init__(self):
        self.linhas = 6
        self.colunas = 6
        self.total_navios = 5
        self.total_submarinos = 3
        self.tabuleiro = Tabuleiro(self.linhas, self.colunas, self.total_navios, self.total_submarinos)
        self.jogadas = 0    #variavel que conta o número de jogadas
        self.tentativas = set()
    #função que inicia o jogo e tem toda a lógica de interação com o usuário
    def jogar(self):
        while True:
            imprimir_tabuleiro(self.tabuleiro, revelar=False)
            print(f"\nJogadas até agora: {self.jogadas}")
            navios_af, subs_af = contar_afundados(self.tabuleiro.posicaoEmbarcacoes)
            print(f"Afundados até agora = Navios {navios_af} de {self.total_navios} | Submarinos {subs_af} de {self.total_submarinos}")
            entrada = input("Digite a posição para tentar (formato A0)\nSe quiser desistir digite -1: ").strip().upper()
            

            if entrada == "-1": #verifica se o usuário quer desistir durante o jogo
                print("Você desistiu. Fim de jogo.")
                break
            # prevenção de entradas inválidas
            coordenada = ler_coordenada(entrada)
            if coordenada is None:
                print("Entrada inválida.")
                continue

            i, j = coordenada
            if not (0 <= i < self.linhas and 0 <= j < self.colunas):
                print("Coordenada fora dos limites.")
                continue

            if (i, j) in self.tentativas:
                print("Você já tentou essa posição.")
                continue
            
            self.jogadas += 1 #adiciona 1 a ao contador de jogadas a cada tentativa
            self.tentativas.add((i, j))#armazena a coordenada já jogada para não repetir

            if self.tabuleiro.getPosicao(i, j) == 1:
                print("💥 Acertou!")
                self.tabuleiro.setPosicao(i, j, 9)
                nome_barco = self.tabuleiro.indiceReversoPosicoesBarcos[(i, j)]
                self.tabuleiro.posicaoEmbarcacoes[nome_barco][(i, j)] = 0
            else:
                print("💦 Errou...")
                self.tabuleiro.setPosicao(i, j, 8)

            navios_af, subs_af = contar_afundados(self.tabuleiro.posicaoEmbarcacoes)
            print(f"Afundados até agora = Navios {navios_af} de {self.total_navios} | Submarinos {subs_af} de {self.total_submarinos}")

            if navios_af == self.total_navios and subs_af == self.total_submarinos:
                print("\n******* Você Ganhou !!!!!! *******")
                imprimir_tabuleiro(self.tabuleiro, revelar=True)
                nome = input("\nMelhores pontuações\nDigite seu nome: ").strip()
                salvar_pontuacao(nome, self.jogadas)
                mostrar_ranking()
                break

    def menu(self):
        print("carregando o Guia do comandante...")
        sleep(1)
        print("\n⚓ ===== Guia do Comandante ===== ⚓")
        mostrarCaracteresUsados()
        while True:
            print("\n***** Batalha Naval *****")
            print("[1] - Jogar")
            print("[2] - Ver Melhores Pontuações")
            print("[3] - tutorial")
            print("[4] - Sair")
            escolha = input("Escolha uma opção: ").strip()

            if escolha == "1":
                print("Iniciando o jogo...")
                sleep(1)
                self.__init__()#inicializa o jogo dnv pro caso do usuário querer jogar dnv(correção erro do tabuleiro =)
                self.jogar()
            elif escolha == "2":
                print("Carregando o ranking...")
                sleep(1)
                mostrar_ranking()
            elif escolha == "3":
                print("abrindo tutorial...\n")
                sleep(1)
                tutorial()
            elif escolha == "4":
                print("Saindo do jogo...")
                return None
            else:
                print("Opção inválida. Tente novamente.")
