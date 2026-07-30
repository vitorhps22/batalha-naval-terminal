ARQUIVO_RANKING = "ranking.txt"

def carregar_ranking():
    try:
        with open(ARQUIVO_RANKING, "r", encoding="utf-8") as arquivo:#utf-8 corrige o problema dos acentos
            ranking = []
            for linha in arquivo:
                nome, jogadas = linha.strip().split(";")
                ranking.append((nome, int(jogadas)))
            return ranking
    except FileNotFoundError:
        return []

def salvar_pontuacao(nome, jogadas):
    ranking = carregar_ranking()
    ranking.append((nome, jogadas))
    ranking.sort(key=lambda x: x[1])#pega o valor das jogadas e usa para ordenar
    ranking = ranking[:10]  # Mantém apenas os 10 melhores
    with open(ARQUIVO_RANKING, "w", encoding="utf-8") as arquivo:
        for nome, jogadas in ranking:
            arquivo.write(f"{nome};{jogadas}\n")

def mostrar_ranking():
    ranking = carregar_ranking()
    print("\n===== Melhores Pontuações =====")
    if not ranking:
        print("Nenhuma pontuação registrada ainda.")
        return

    print(f"{'Nome':<10} {'# Jogadas'}")
    for i, (nome, jogadas) in enumerate(ranking[:10], start=1):
        print(f"{i}. {nome:<10} {jogadas}")
