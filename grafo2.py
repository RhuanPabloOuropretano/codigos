import networkx as nx
import matplotlib.pyplot as plt

# Função para desenhar o grafo
def desenhar_grafo(arestas):
    # Criação do grafo
    G = nx.Graph()

    # Adicionando as arestas
    G.add_edges_from(arestas)

    # Desenhando o grafo
    pos = nx.spring_layout(G)  # layout para uma disposição visual mais clara
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15, font_color='black', font_weight='bold', edge_color='gray')
    plt.title("Representação gráfica do Grafo")
    plt.show()

# Definição das arestas
arestas = [(1, 2), (1, 4), (1, 6), (1, 7), (1, 8), (1, 9), (2, 5),(2, 6),(2, 7),(3, 4),(3, 8),(3, 9),(4, 6),(4, 9),(5, 6),(5, 7),(7, 8),(8, 9)]

# Chamando a função para desenhar o grafo
desenhar_grafo(arestas)
