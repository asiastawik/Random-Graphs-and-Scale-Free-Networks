# Random Graphs and Scale-Free Networks

This project implements various random graph models and analyzes their properties. The following models are covered:

1. **Erdős-Rényi G(N, L)**: A random graph with `N` nodes and `L` randomly placed links.
2. **Gilbert G(N, p)**: A random graph where each pair of nodes is connected with probability `p`.
3. **Watts-Strogatz Model (WS)**: A small-world network model that begins with a regular ring lattice and rewires links with a certain probability `β`.
4. **Barabási-Albert Model**: A scale-free network model that generates networks with a power-law degree distribution.

## Project Structure
## Implementation Overview

### Models

1. **Erdős-Rényi Model (G(N, L))**
   - Generates a random graph with `N` nodes and `L` edges.
   
2. **Gilbert Model (G(N, p))**
   - Creates a random graph by connecting each pair of nodes with a probability `p`.

3. **Watts-Strogatz Model (WS(N, k, β))**
   - Starts with a ring of `N` nodes where each node is connected to its `k` nearest neighbors. Links are rewired with probability `β`.

4. **Barabási-Albert Model**
   - Implements a network that grows over time, maintaining a power-law distribution of connections.

### Analysis

For each graph type, the following properties will be calculated and plotted:

- **Degree Distribution**: \( P(k) \) and average degree \( \langle k \rangle \)
- **Clustering Coefficient**: Distribution and average clustering coefficient
- **Shortest Paths**: Distribution, diameter, and average path length

### Watts-Strogatz Analysis

1. **Average Path Length and Clustering Coefficient**:
   - Analyze how these metrics change with different values of \( β \) for `N = 1000` and `k = 4, 8`.
   - Compare results with those in the Network Science book.

2. **Scaling Properties**:
   - Calculate the diameter \( d_{max} \) and average path length \( \langle d \rangle \) for different values of \( N \) and plot how these scale with \( N \).

### Barabási-Albert Model Analysis

1. **Graph Visualization**:
   - Draw the graph with nodes colored based on their degree (odd/even) and size scaled by degree.

2. **Degree Distribution**:
   - Calculate and plot the degree distribution for \( N = 10^7 \).

3. **Shortest Path Length**:
   - Calculate and plot the PDF of the shortest path lengths for \( N = 10^7 \).

4. **Clustering Coefficient PDF**:
   - Calculate and plot the PDF of the clustering coefficients for \( N = 10^7 \).
