import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import qiskit
from qiskit import *

from qiskit.tools.visualization import plot_histogram
from qiskit_aqua import Operator, run_algorithm, get_algorithm_instance
from qiskit_aqua.input import get_input_instance
from qiskit_aqua.translators.ising import maxcut, tsp

# nodes 
n = 20

