#Autômato Finito
#Lucas Luiz Moreira Urani

# Função para encontrar todos os caminhos em um grafo
def find_all_paths(graph, start, end, path=[]):
    # Adiciona o nó atual ao caminho
    path = path + [start]
    # Se o nó atual for o nó final, retorna o caminho
    if start == end:
        return [path]
    # Se o nó atual não estiver no grafo, retorna uma lista vazia
    if start not in graph:
        return []
    # Lista para armazenar todos os caminhos possíveis
    paths = []
    # Para cada nó conectado ao nó atual
    for node in graph[start]:
        # Se o nó não estiver no caminho
        if node not in path:
            # Encontra todos os caminhos a partir desse nó
            new_paths = find_all_paths(graph, node, end, path)
            # Adiciona os novos caminhos à lista de caminhos
            for new_path in new_paths:
                paths.append(new_path)
    # Retorna todos os caminhos possíveis
    return paths

# Grafo representando o autômato finito livre de contexto
grafo = {
    "Inicio": ["Caverna", "Piratas"],
    "Caverna": ["Floresta", "Inicio"],
    "Piratas": ["Colinas", "Acampamento"],
    "Acampamento": [],
    "Colinas": ["Caverna", "Montanhas"],
    "Floresta": ["Colinas", "Montanhas"],
    "Montanhas": ["Animais", "Tesouro"],
    "Animais": []
}

# Encontrar todos os caminhos possíveis no AFDC
todos_caminhos = find_all_paths(grafo, "Inicio", "Tesouro")

# Encontrar caminhos que levam a Acampamento
caminhos_para_acampamento = find_all_paths(grafo, "Inicio", "Acampamento")

# Encontrar caminhos que levam a Animais
caminhos_para_animais = find_all_paths(grafo, "Inicio", "Animais")

# Encontrar o caminho mais rápido
caminho_rapido = min(todos_caminhos, key=len)

# Encontrar o caminho mais longo
caminho_longo = max(todos_caminhos, key=len)

# Mostrar os resultados
print("Todos os caminhos:")
# Imprime todos os caminhos e o número de transições
for caminho in todos_caminhos:
    print(" -> ".join(caminho), f"({len(caminho)-1} transições)")
print("\nCaminho mais rápido:", " -> ".join(caminho_rapido), f"({len(caminho_rapido)-1} transições)")
print("\nCaminho mais longo:", " -> ".join(caminho_longo), f"({len(caminho_longo)-1} transições)")

# Mostrar caminhos que levam a Acampamento
print("\nCaminhos que levam a Acampamento (Fim de jogo):")
# Imprime os caminhos para Acampamento e o número de transições
for caminho_acampamento in caminhos_para_acampamento:
    print(" -> ".join(caminho_acampamento), f"({len(caminho_acampamento)-1} transições)")

# Mostrar caminhos que levam a Animais
print("\nCaminhos que levam a Animais (Fim de jogo):")
# Imprime os caminhos para Animais e o número de transições
for caminho_animais in caminhos_para_animais:
    print(" -> ".join(caminho_animais), f"({len(caminho_animais)-1} transições)")
