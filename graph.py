import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import qiskit
from qiskit import *

from qiskit.tools.visualization import plot_histogram
from qiskit_aqua import Operator, run_algorithm, get_algorithm_instance
from qiskit_aqua.input import get_input_instance
from qiskit_aqua.translators.ising import maxcut, tsp

from qiskit import QuantumCircuit, 

# nodes 
n = 20

#Graph Model with Edges (basic)
G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3])
G.add_edges_from([(0, 1), (1, 2)])
nx.draw(G, with_labels=True, alpha=0.8, node_size=500)


