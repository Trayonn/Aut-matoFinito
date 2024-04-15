#Autômato Finito CC_D1
#Lucas Luiz Moreira Urani, Kauan Mendes Caetano, Guilherme Bastos, João Victor Souza


# Função para exibir as opções disponíveis
def exibir_opcoes(ponto_atual):
    opcoes = {
        "Inicio": "Você está no Início. Escolha para onde ir:\nA - Caminho a direita\nB - Caminho a esquerda",
        "Caverna": "Você chegou em um local com diversas cavernas. Escolha para onde ir:\nA - Caminho a direita\nB - Caminho a esquerda",
        "Piratas": "Você chegou em um campo de piratas, você escuta conversas sobre um grupo de foragidos acampando a bombordo dessa localização. Escolha para onde ir:\nA - Caminho a direita\nB - Caminho a esquerda",
        "Acampamento": "Você cruzou caminho com os foragidos. CUIDADO! É uma armadilha! O jogo acabou!",
        "Colinas": "Você chega a duas pequenas colinas, na sua esquerda há uma estrada de terra que leva a diversas montanhas, na sua direita você observa entradas de cavernas. Escolha pra onde ir: \nA- Caminho a direita\nB - Caminho a esquerda",
        "Floresta": "Saindo da caverna, você se encontra em uma extensa floresta. Escolha para onde ir:\nA- Caminho a direita\nB- Caminho a esquerda",
        "Montanhas": "Você chega a uma cordilheira, você escuta o barulho de animais muito perto de você. Escolha para onde ir: \nA- Caminho a direita\nB- Caminho a esquerda",
        "Animais": "Você pegou o caminho mais curto e se deparou com animais selvagens. O jogo acabou!",
        "Tesouro": "Você chegou ao local que estava descrito no seu mapa, o tesouro é seu! Parabéns! "
        
    }
    print(opcoes.get(ponto_atual, "Local desconhecido."))

# Definição do ponto atual
ponto_atual = "Inicio"

# Loop principal
while True:
    # Exibir opções disponíveis
    exibir_opcoes(ponto_atual)

    # Obter escolha do jogador
    escolha = input("Escolha (A/B): ").upper()

    # Verificar se o ponto atual é uma armadilha (fim de jogo)
    if ponto_atual == "Estrada":
        print("Você caiu em uma armadilha! O jogo acabou!")
        break
    if ponto_atual == "Animais":
        print("Você foi pego pelos animais! O jogo acabou!")
        break

    #Verifica se o jogador ganhou.
    if ponto_atual == "Tesouro":
        print("Você achou o tesouro! O jogo acabou!")
        break


    # Atualizar o ponto atual com base na escolha do jogador
    pontos_proximos = {
        ("Inicio", "A"): "Caverna",
        ("Inicio", "B"): "Piratas",
        ("Caverna", "A"): "Floresta",
        ("Caverna", "B"): "Inicio",
        ("Piratas", "A"): "Colinas",  
        ("Piratas", "B"): "Acampamento", #armadilha
        ("Colinas", 'A'): "Caverna",
        ("Colinas", 'B'): "Montanhas",
        ("Floresta", 'A'): "Colinas",
        ("Floresta", 'B'): "Montanhas", 
        ("Montanhas", 'A'): "Animais", #Armadilha
        ("Montanhas", 'B'): "Tesouro",
        # 
    }
    ponto_atual = pontos_proximos.get((ponto_atual, escolha), "Escolha inválida.")

# Verificar se o jogador foi redirecionado de volta para o início
    if ponto_atual == "Inicio" and escolha == "B":
        print("Você se perdeu e acabou voltando para o inicio.")
