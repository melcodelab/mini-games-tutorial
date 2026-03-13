# 🐍 Jogo da Cobrinha

Um jogo clássico de cobrinha desenvolvido em **Python** com **Pygame**. Projeto criado como treino em desenvolvimento de games, seguindo um tutorial prático.

> Tutorial seguido: [Jogo Snake em Python - Criando o Jogo da Cobrinha com PyGame [Tutorial Completo] - Canal Hashtag Programação](https://www.youtube.com/watch?v=bgsmYOm-W80)

### Objetivo
1. Guie a cobrinha para comer a comida (quadrados vermelhos)
2. A cada comida consumida, a cobra cresce e sua pontuação aumenta
3. Evite bater nas paredes (bordas da tela) ou mover a cobra para a a direção contrária que ela está se movendo (por exemplo, se ela estiver indo para cima e você apertar para ela ir pra baixo, você perde)
4. Continue o máximo de tempo possível.

## Requisitos

- Python 3.7 ou superior
- Pygame

## Instalação

### 1. Clonar ou baixar o projeto
```bash
cd seu-diretorio/mini-games-tutorial/game-snake
```

### 2. Instalar o Pygame
```bash
pip install pygame
```

## Como Executar

Execute o jogo com:
```bash
python main.py
```

Ou:
```bash
python3 main.py
```

A janela do jogo com 1000x800 pixels abrirá automaticamente, para iniciar o jogo basta apertar nas teclas do teclado.

## Estrutura do Projeto

```
game-snake/
├── main.py          # Arquivo principal que inicia o jogo
├── game.py          # Funções de lógica e renderização do jogo
└── README.md        # Este arquivo
```
