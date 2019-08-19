import networkx as nx
from random import sample, randint
from math import sqrt
from node import is_node_infected, set_node_infected

def new_wave(graph: nx.Graph):
	for node in filter(lambda node: is_node_infected(graph, node), graph.nodes):
		pass