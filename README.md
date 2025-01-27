# Jogo de Aventura com Autômato Finito
Este é um jogo de aventura baseado em um autômato finito. O jogo simula uma jornada por diferentes locais em um mapa, com decisões a serem tomadas pelo jogador. O jogo possui dois códigos principais:

- automato.py: Este código define o autômato finito e encontra todos os caminhos possíveis em um grafo que representa as opções de movimento.
- index.py: O código principal do jogo, onde o jogador interage com o sistema e toma decisões para avançar pelos caminhos, até chegar a um final.

## Descrição do Jogo
O jogo simula uma jornada onde o jogador precisa tomar decisões para explorar diferentes locais em busca de um tesouro. O objetivo é evitar armadilhas e encontrar o tesouro antes de ser pego por animais selvagens ou cair em armadilhas.

## Locais no Mapa
O mapa é composto por diversos locais interconectados, representados por um grafo. O jogador pode escolher entre duas opções em cada local, representadas pelas opções "A" ou "B". Cada escolha leva a um novo local ou a um final do jogo.

- Início: O ponto de partida.
- Caverna: Um local com diversas cavernas.
- Piratas: Um campo com piratas.
- Acampamento: Uma armadilha! (Fim de jogo)
- Colinas: Duas pequenas colinas, com opções para outros locais.
- Floresta: Uma floresta densa.
- Montanhas: Uma cordilheira onde o jogador ouve os animais selvagens.
- Animais: Uma armadilha! (Fim de jogo).
- Tesouro: O objetivo do jogo, onde o tesouro é encontrado (Fim de jogo).
  
## Como Funciona

O autômato finito modela as possíveis transições entre os locais, e o jogo utiliza essas transições para guiar o jogador. O código automato.py é responsável por calcular e exibir todos os caminhos possíveis, além de identificar o caminho mais curto e o mais longo.  

O código index.py permite que o jogador interaja com o jogo, fazendo escolhas em cada ponto da jornada, e o jogo é finalizado quando o jogador chega ao tesouro ou cai em uma armadilha.
