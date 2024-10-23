#Network - set of nodes and set of relations between these nodes - links
#Represented as matrix, list, graphs...
#Links are bidiagonal

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#a - G(N,L)
def create_random_graph_ER(N, L):
    G = nx.Graph() #empty graph object
    G.add_nodes_from(range(N))
    
    if L > N*(N-1)//2:
        raise ValueError("Number of links (L) exceeds the maximum possible for the given number of nodes (N).")
    
    while G.number_of_edges() < L:
        node1 = np.random.randint(0, N)
        node2 = np.random.randint(0, N)
        
        if node1 != node2 and not G.has_edge(node1, node2):
            G.add_edge(node1, node2)
    
    return G

N = 10 #number of nodes
L = 15 #number of edges

G_a = create_random_graph_ER(N, L)

pos = nx.spring_layout(G_a) #position of nodes
nx.draw(G_a, pos, with_labels=True)
plt.show()

degree_sequence_a = list(dict(G_a.degree()).values())
degree_count_a = np.bincount(degree_sequence_a)
degree_prob_a = degree_count_a / degree_count_a.sum()

average_degree_a = np.mean(degree_sequence_a)

plt.bar(range(len(degree_prob_a)), degree_prob_a)
plt.xlabel('Degree <k>')
plt.ylabel('Probability')
plt.title('Degree Distribution - Model (a)')
plt.show()

print("Average Degree (Model a):", average_degree_a)


#b - G(N,p)
def create_random_graph_G(N, p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    for node1 in range(N):
        for node2 in range(node1+1, N):
            if np.random.random() < p:
                G.add_edge(node1, node2)
    
    return G

N = 10
p = 0.5 #probability

G_b = create_random_graph_G(N, p)

pos = nx.spring_layout(G_b)
nx.draw(G_b, pos, with_labels=True)
plt.show()

degree_sequence_b = list(dict(G_b.degree()).values())
degree_count_b = np.bincount(degree_sequence_b)
degree_prob_b = degree_count_b / degree_count_b.sum()

average_degree_b = np.mean(degree_sequence_b)

plt.bar(range(len(degree_prob_b)), degree_prob_b)
plt.xlabel('Degree <k>')
plt.ylabel('Probability')
plt.title('Degree Distribution - Model (b)')
plt.show()

print("Average Degree (Model b):", average_degree_b)

#c - G(N,k,beta)
def create_small_world_graph_WS(N, k, beta):
    G = nx.Graph()
    nodes = range(N)
    G.add_nodes_from(nodes)
    
    for i in range(N):
        for j in range(1, k//2+1):
            neighbor = (i+j) % N
            G.add_edge(i, neighbor)
    
    for i in range(N):
        for j in range(1, k//2+1):
            if np.random.random() < beta: #rewired some edges with a probability beta
                new_neighbor = np.random.choice(nodes) #new neighbor randomly chosen
                while new_neighbor == i or G.has_edge(i, new_neighbor):
                    new_neighbor = np.random.choice(nodes)
                old_neighbor = (i+j) % N
                G.remove_edge(i, old_neighbor) #delete old edge
                G.add_edge(i, new_neighbor) #add new one
    
    return G

N = 20
k = 4 #neighbors
beta = 0.2 #probability

G_c = create_small_world_graph_WS(N, k, beta)

pos = nx.spring_layout(G_c)
nx.draw(G_c, pos, with_labels=True)
plt.show()

degree_sequence_c = list(dict(G_c.degree()).values())
degree_count_c = np.bincount(degree_sequence_c)
degree_prob_c = degree_count_c / degree_count_c.sum()

average_degree_c = np.mean(degree_sequence_c)

plt.bar(range(len(degree_prob_c)), degree_prob_c)
plt.xlabel('Degree <k>')
plt.ylabel('Probability')
plt.title('Degree Distribution - Model (c)')
plt.show()

print("Average Degree (Model c):", average_degree_c)

# Model (a) - Erdos-Renyi random graph (N, L)
clustering_coefficients_a = nx.clustering(G_a)
average_clustering_coefficient_a = nx.average_clustering(G_a)

#print("Clustering Coefficients (Model a):", clustering_coefficients_a)
print("Average Clustering Coefficient (Model a):", average_clustering_coefficient_a)
plt.hist(list(clustering_coefficients_a.values()), bins=10)
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.title('Distribution of Clustering Coefficients - Model (a)')
plt.show()


# Model (b) - Gilbert random graph (N, p)
clustering_coefficients_b = nx.clustering(G_b)
average_clustering_coefficient_b = nx.average_clustering(G_b)

#print("Clustering Coefficients (Model b):", clustering_coefficients_b)
print("Average Clustering Coefficient (Model b):", average_clustering_coefficient_b)
plt.hist(list(clustering_coefficients_b.values()), bins=10)
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.title('Distribution of Clustering Coefficients - Model (b)')
plt.show()


# Model (c) - Watts-Strogatz small-world graph (N, k, beta)
clustering_coefficients_c = nx.clustering(G_c)
average_clustering_coefficient_c = nx.average_clustering(G_c)

#print("Clustering Coefficients (Model c):", clustering_coefficients_c)
print("Average Clustering Coefficient (Model c):", average_clustering_coefficient_c)
plt.hist(list(clustering_coefficients_c.values()), bins=10)
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.title('Distribution of Clustering Coefficients - Model (c)')
plt.show()

# Model (a) - Erdos-Renyi random graph (N, L)
shortest_paths_a = dict(nx.all_pairs_shortest_path_length(G_a))
path_lengths_a = []
for paths in shortest_paths_a.values():
    for length in paths.values():
        path_lengths_a.append(length)
        
diameter_a = np.max(path_lengths_a)
average_path_length_a = np.mean(path_lengths_a)

#print("Shortest Paths (Model a):", shortest_paths_a)
print("Diameter (Model a):", diameter_a)
print("Average Path Length (Model a):", average_path_length_a)
plt.hist(path_lengths_a, bins=10)
plt.xlabel('Shortest Path Length')
plt.ylabel('Frequency')
plt.title('Distribution of Shortest Paths - Model (a)')
plt.show()


# Model (b) - Gilbert random graph (N, p)
shortest_paths_b = dict(nx.all_pairs_shortest_path_length(G_b))
path_lengths_b = []
for paths in shortest_paths_b.values():
    for length in paths.values():
        path_lengths_b.append(length)
        
diameter_b = np.max(path_lengths_b)
average_path_length_b = np.mean(path_lengths_b)

#print("Shortest Paths (Model b):", shortest_paths_b)
print("Diameter (Model b):", diameter_b)
print("Average Path Length (Model b):", average_path_length_b)
plt.hist(path_lengths_b, bins=10)
plt.xlabel('Shortest Path Length')
plt.ylabel('Frequency')
plt.title('Distribution of Shortest Paths - Model (b)')
plt.show()


# Model (c) - Watts-Strogatz small-world graph (N, k, beta)
shortest_paths_c = dict(nx.all_pairs_shortest_path_length(G_c))
path_lengths_c = []
for paths in shortest_paths_c.values():
    for length in paths.values():
        path_lengths_c.append(length)
        
diameter_c = np.max(path_lengths_c)
average_path_length_c = np.mean(path_lengths_c)

#print("Shortest Paths (Model c):", shortest_paths_c)
print("Diameter (Model c):", diameter_c)
print("Average Path Length (Model c):", average_path_length_c)
plt.hist(path_lengths_c, bins=10)
plt.xlabel('Shortest Path Length')
plt.ylabel('Frequency')
plt.title('Distribution of Shortest Paths - Model (c)')
plt.show()

#For what values of parameters does it make sense to compare these models?
'''
If one model has a much larger or smaller number of nodes than the others, the resulting graphs may have significantly different properties.
If the number of links or link probability differs significantly, the resulting graphs may have different levels of connectivity.
If the initial degree or rewiring probability differs significantly, the resulting graphs may exhibit different levels of clustering and small-worldness.
'''