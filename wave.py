import networkx as nx
from random import sample, randint
from math import sqrt

def new_wave(graph: nx.Graph):
	for node in sample(graph.nodes, randint(0, int(sqrt(graph.number_of_nodes())))):
		nx.set_node_attributes(graph, { node: { 'infected': True } })