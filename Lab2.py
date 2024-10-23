import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#from task 1
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

# a
def calculate_WS_graph(N, k, beta):
    #G = nx.watts_strogatz_graph(N, k, beta) #function in networkx lib
    #or
    G = create_small_world_graph_WS(N, k, beta)
    average_path_length = nx.average_shortest_path_length(G)
    average_clustering_coefficient = nx.average_clustering(G)
    diameter = nx.diameter(G)
    return average_path_length, average_clustering_coefficient, diameter

N = 100
k_values = [4, 8]
beta_values = np.linspace(0, 1, 11)  #11 points from 0 to 1
    
average_path_lengths = []
average_clustering_coefficients = []
    
for k in k_values:
    avg_path_lengths = []
    avg_clustering_coeffs = []

    for beta in beta_values:
        avg_path_length, avg_clustering_coefficient, diameter = calculate_WS_graph(N, k, beta)
        avg_path_lengths.append(avg_path_length)
        avg_clustering_coeffs.append(avg_clustering_coefficient)

    average_path_lengths.append(avg_path_lengths)
    average_clustering_coefficients.append(avg_clustering_coeffs)


plt.plot(beta_values, average_path_lengths[0], label=f'k = {k_values[0]}')
plt.plot(beta_values, average_path_lengths[1], label=f'k = {k_values[1]}')
plt.xlabel('Probability β')
plt.ylabel('Average Path Length')
plt.title('Average Path Length as a function of β')
plt.legend()
plt.show()

plt.plot(beta_values, average_clustering_coefficients[0], label=f'k = {k_values[0]}')
plt.plot(beta_values, average_clustering_coefficients[1], label=f'k = {k_values[1]}')
plt.xlabel('Probability β')
plt.ylabel('Average Clustering Coefficient')
plt.title('Average Clustering Coefficient as a function of β')
plt.legend()
plt.show()

# b
k = 4
N_values = [100, 500, 1000, 2000, 5000]
beta = 0.2

diameters = []
average_path_lengths = []

for N in N_values:
    avg_path_length, avg_clustering_coeff, diameter = calculate_WS_graph(N, k, beta)
    diameters.append(diameter)
    average_path_lengths.append(avg_path_length)
    dmax = np.log(N) / np.log(k)
    d = np.log(N) / np.log(k)

plt.plot(N_values, diameters, 'o-')
plt.xlabel('N')
plt.ylabel('Diameter (dmax)')
plt.title('Diameter Scaling with N')
plt.show()

plt.plot(N_values, average_path_lengths, 'o-')
plt.xlabel('N')
plt.ylabel('Average Path Length (<d>)')
plt.title('Average Path Length Scaling with N')
plt.show()

#theoretical values
theory_diameters = np.log(N_values) / np.log(k)
theory_average_path_lengths = np.log(N_values) / np.log(k)

plt.plot(N_values, average_path_lengths, '-', label='Real')
plt.plot(N_values, theory_average_path_lengths, '--', label='Theoretical')
plt.xlabel('N')
plt.ylabel('Path Length (<d>)')
plt.title('Path Length Scaling with N')
plt.legend()
plt.show()

