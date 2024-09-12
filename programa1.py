class Grafo:
    def __init__(self):
        self.grafo = {}

    # Função para adicionar uma aresta ao grafo (não-direcionado)
    def adicionar_aresta(self, origem, destino):
        # Adiciona a aresta de origem para destino
        if origem not in self.grafo:
            self.grafo[origem] = []
        self.grafo[origem].append(destino)

        # Como o grafo é não-direcionado, adiciona a aresta de destino para origem
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[destino].append(origem)

    # Função para exibir o grafo
    def exibir_grafo(self):
        for vertice in self.grafo:
            print(f"{vertice} -> {' -> '.join(map(str, self.grafo[vertice]))}")

# Exemplo de uso
if __name__ == "__main__":
    # Criação do grafo
    grafo = Grafo()

    # Adicionando arestas
    grafo.adicionar_aresta(1, 2)
    grafo.adicionar_aresta(1, 4)
    grafo.adicionar_aresta(1, 6)
    grafo.adicionar_aresta(1, 7)
    grafo.adicionar_aresta(1, 8)
    grafo.adicionar_aresta(1, 9)
    grafo.adicionar_aresta(2, 5)
    grafo.adicionar_aresta(2, 6)
    grafo.adicionar_aresta(2, 7)
    grafo.adicionar_aresta(3, 4)
    grafo.adicionar_aresta(3, 8)
    grafo.adicionar_aresta(3, 9)
    grafo.adicionar_aresta(4, 6)
    grafo.adicionar_aresta(4, 9)
    grafo.adicionar_aresta(5, 6)
    grafo.adicionar_aresta(5, 7)
    grafo.adicionar_aresta(7, 8)
    grafo.adicionar_aresta(8, 9)
    # Exibindo o grafo
    grafo.exibir_grafo()
