import networkx as nx
import time

# 1. Instanciando um Grafo Não Direcionado
G = nx.Graph()

# 2. Consolidando as arestas (estrutura original mantida)
# Formato: (Nó de Origem, Nó de Destino, Peso)
arestas = [
    ('O', '4', 60), ('Z', '1', 90), ('C', '2', 110),
    ('O', 'E', 65), ('P', 'V', 420), ('2', 'D', 100),
    ('4', 'E', 60), ('1', 'A', 90), ('1', '2', 130),
    ('F', 'W', 170), ('A', 'B', 70), ('P', 'B', 210),
    ('F', 'P', 350), ('A', '2', 110), ('P', 'D', 320),
    ('E', 'W', 140), ('B', 'C', 65), ('P', 'Q', 450),
    ('E', '1', 260), ('B', '2', 100), ('2', '3', 130), ('D', 'Q', 270),
    ('Z', 'P', 180), ('C', 'D', 65), ('D', '3', 140), ('3', 'Q', 320)
]

G.add_weighted_edges_from(arestas)

# 3. Definindo Origem e Destino
start_node = 'A'
target_node = 'E'

# 4. Definindo a Heurística Admissível
def heuristica_nula(u, v):
    """
    Como os nós não possuem coordenadas X, Y reais para calcular a distância
    em linha reta, retornamos 0. Isso garante que a heurística nunca superestime
    o custo, mantendo o A* perfeito.
    """
    return 0

# Registre o tempo imediatamente antes da execução
inicio = time.perf_counter()

# 5. Executando o algoritmo A* nativo do NetworkX
# astar_path retorna a sequência de vértices da melhor rota
rota = nx.astar_path(G, source=start_node, target=target_node, heuristic=heuristica_nula, weight='weight')

# astar_path_length retorna a soma dos pesos dessa rota
custo = nx.astar_path_length(G, source=start_node, target=target_node, heuristic=heuristica_nula, weight='weight')
fim = time.perf_counter()

# Calcule a diferença
tempo_execucao = fim - inicio

# 6. Saída de dados formatada
print("=== RESULTADO DO ALGORITMO A* ===")
print(f"Origem: {start_node} | Destino: {target_node}")
print(f"Melhor Caminho (Nós visitados): {' -> '.join(rota)}")
print(f"Custo Total da Rota: {custo}")

# Exibe o tempo em segundos e milissegundos
print(f"Tempo de execução: {tempo_execucao:.6f} segundos ({tempo_execucao * 1000:.3f} ms)")