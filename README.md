# Batalha Naval Terminal

Jogo de Batalha Naval jogado no terminal, desenvolvido em Python. O projeto apresenta tabuleiro, interface de texto e ranking de melhores pontuações.

## Recursos

- Tabuleiro 6x6
- Navios de 1 célula e submarinos de 2 células
- Entrada de coordenadas no formato `A0`, `B3` etc.
- Ranking local de melhores pontuações salvo em `ranking.txt`
- Tutorial dentro do jogo
- Interface de exibição simples no terminal

## Estrutura do projeto

- `main.py`: ponto de entrada do jogo.
- `FrontEnd.py`: lógica de menu, controle do fluxo do jogo e da interação com o jogador.
- `Exibicao.py`: funções para desenhar o tabuleiro no terminal e mostrar os símbolos usados.
- `Tabuleiro.py`: geração e posicionamento aleatório de embarcações no tabuleiro.
- `Persistencia.py`: gravação e leitura do ranking de pontuação.

## Como executar

1. Certifique-se de ter Python 3 instalado.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python main.py
```

## Como jogar

- No menu, escolha `1` para iniciar o jogo.
- Informe a coordenada no formato `A0`, `B3`, `E5`, etc.
- Use `-1` para desistir a qualquer momento.
- O jogo exibe se você acertou ou errou.
- Quando todos os navios e submarinos forem afundados, você pode salvar seu nome no ranking.

## Ranking

- O ranking é salvo no arquivo `ranking.txt`.
- O jogo mantém até as 10 melhores pontuações (menos jogadas são melhores).
- Opção `2` no menu mostra o ranking atual.

## Observações

- O tabuleiro é reiniciado automaticamente ao começar uma nova partida.
- Submarinos ocupam duas posições conectadas horizontalmente ou verticalmente.
- Navios ocupam apenas uma posição.

## Dependências

- Nenhuma biblioteca externa necessária.
- Compatível com Python 3.
