import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

#scale-free Barabasi-Albert graphs

# a
def draw_graph(G):
    pos = nx.spring_layout(G)
    even_nodes = []
    odd_nodes = []
    
    for node in G.nodes:
        if G.degree[node] % 2 == 0:
            even_nodes.append(node)
        else:
            odd_nodes.append(node)
    
    nx.draw_networkx_nodes(G, pos, nodelist=even_nodes, node_color='blue', node_size=100)
    nx.draw_networkx_nodes(G, pos, nodelist=odd_nodes, node_color='red', node_size=100)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.show()

# b
def draw_graph_with_size(G):
    pos = nx.spring_layout(G)
    node_sizes = []
    for node in G.nodes:
        size = 10 * G.degree[node] #scale 10 times
        node_sizes.append(size)
    
    nx.draw_networkx_nodes(G, pos, node_color='blue', node_size=node_sizes)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.show()

# c
def plot_degree_distribution(G):
    degrees = []
    for node in G.nodes:
        degrees.append(G.degree[node])
        
    degree_counts = np.bincount(degrees)
    degree_probs = degree_counts / np.sum(degree_counts)

    plt.plot(range(len(degree_probs)), degree_probs, 'o')
    plt.xlabel('Degree (k)')
    plt.ylabel('Probability P(k)')
    plt.title('Degree Distribution')
    plt.show()

# d
def plot_shortest_path_length_pdf(G):
    shortest_path_lengths = []

    for node1 in G.nodes:
        for node2 in G.nodes:
            if node1 != node2:
                shortest_path_lengths.append(nx.shortest_path_length(G, node1, node2))

    plt.hist(shortest_path_lengths, bins=10, density=True)
    plt.xlabel('Shortest Path Length')
    plt.ylabel('Probability')
    plt.title('PDF of Shortest Path Length')
    plt.show()

# e
def plot_clustering_coefficient_pdf(G):
    clustering_coefficients = list(nx.clustering(G).values())

    plt.hist(clustering_coefficients, bins=30, density=True)
    plt.xlabel('Clustering Coefficient')
    plt.ylabel('Probability')
    plt.title('PDF of Clustering Coefficients')
    plt.show()


# Create a Barabási-Albert graph

N = 10**3
#N = 10**7
m = 5
G = nx.barabasi_albert_graph(N, m)
# #print('done')

draw_graph(G)
draw_graph_with_size(G)

N2 = 10**3
G2 = nx.barabasi_albert_graph(N2, m)
#print('done2')

plot_degree_distribution(G2)
plot_shortest_path_length_pdf(G2)
plot_clustering_coefficient_pdf(G2)


# Implementation without using networkx lib

# def create_barabasi_albert_graph(N, m):
#     G = dict()
#     nodes = list(range(m))
#     edges = []

#     for i in range(m):
#         for j in range(i + 1, m):
#             edges.append((i, j))

#     for i in range(m, N):
#         G[i] = set()

#         selected_edges = set()
#         while len(selected_edges) < m:
#             edge = random.choice(edges)
#             selected_edges.add(edge)

#         for edge in selected_edges:
#             node1, node2 = edge
#             G[i].add(node1)
#             G[i].add(node2)
#             G[node1].add(i)
#             G[node2].add(i)

#         edges.extend(selected_edges)

#     unused_nodes = set(range(N)) - set(G.keys())
#     for node in unused_nodes:
#         del G[node]

#     return G

# N = 10**3
# m = 5
# G = create_barabasi_albert_graph(N, m)

# N2 = 10**7
# G2 = create_barabasi_albert_graph(N2, m)
