import random

def create_barabasi_albert_graph(N, m):
    G = dict()
    edges = []

    for i in range(m):
        for j in range(i + 1, m):
            edges.append((i, j))

    for i in range(m, N):
        G[i] = set()

        selected_edges = set()
        while len(selected_edges) < m:
            edge = random.choice(edges)
            selected_edges.add(edge)

        for edge in selected_edges:
            node1, node2 = edge
            G[i].add(node1)
            G[i].add(node2)
            G[node1].add(i)
            G[node2].add(i)

        edges.extend(selected_edges)

    unused_nodes = [node for node in G if len(G[node]) == 0]
    for node in unused_nodes:
        del G[node]

    return G

N = 10**3
m = 3
G = create_barabasi_albert_graph(N, m)
