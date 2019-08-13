import networkx as nx
from numpy.random import normal
from constants import *
from EdgeType import EdgeType

def network_size_for_edge_type(edge_type):
	return max(0, round(normal(NETWORK_SIZES[edge_type])))

def add_network(graph, edge_type, num):
	graph.add_edges_from([(num, (num, i)) for i in range(network_size_for_edge_type(edge_type))], edge_type=edge_type)

def create_graph():
	graph = nx.Graph()
	for i in range(NUMBER_OF_LOCAL_WIRED_NETWORKS):
		add_network(graph, EdgeType.LOCAL_WIRED, i)
	for i in range(NUMBER_OF_LOCAL_WIRED_NETWORKS, NUMBER_OF_LOCAL_WIRED_NETWORKS + NUMBER_OF_LOCAL_WIRELESS_NETWORKS):
		add_network(graph, EdgeType.LOCAL_WIRELESS, i)
	for i in range(NUMBER_OF_LOCAL_WIRED_NETWORKS + NUMBER_OF_LOCAL_WIRELESS_NETWORKS):
		graph.add_edge(i, NUMBER_OF_LOCAL_WIRED_NETWORKS + NUMBER_OF_LOCAL_WIRELESS_NETWORKS + 1)
	return graph