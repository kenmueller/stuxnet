import networkx as nx
from numpy.random import normal
from constants import *
from edge_type import EdgeType

NUMBER_OF_LOCAL_WIRED_AND_WIRELESS_NETWORKS = NUMBER_OF_LOCAL_WIRED_NETWORKS + NUMBER_OF_LOCAL_WIRELESS_NETWORKS

def network_size_for_edge_type(edge_type: EdgeType) -> int:
	return max(0, round(normal(NETWORK_SIZES[edge_type])))

def add_network(graph: nx.Graph, edge_type: EdgeType, num: int):
	graph.add_edges_from([(num, (num, i)) for i in range(network_size_for_edge_type(edge_type))], edge_type=edge_type)

def create_graph() -> nx.Graph:
	graph = nx.Graph()
	for i in range(NUMBER_OF_LOCAL_WIRED_NETWORKS):
		add_network(graph, EdgeType.LOCAL_WIRED, i)
	for i in range(NUMBER_OF_LOCAL_WIRED_NETWORKS, NUMBER_OF_LOCAL_WIRED_AND_WIRELESS_NETWORKS):
		add_network(graph, EdgeType.LOCAL_WIRELESS, i)
	for i in range(NUMBER_OF_LOCAL_WIRED_AND_WIRELESS_NETWORKS):
		graph.add_edge(i, NUMBER_OF_LOCAL_WIRED_AND_WIRELESS_NETWORKS)
	return graph