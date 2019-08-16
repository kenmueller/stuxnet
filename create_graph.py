import networkx as nx
from numpy.random import normal
from random import sample
from constants import *
from edge_type import EdgeType

NUMBER_OF_LOCAL_NETWORKS = NUMBER_OF_LOCAL_WIRED_NETWORKS + NUMBER_OF_LOCAL_WIRELESS_NETWORKS

def network_size_for_edge_type(edge_type: EdgeType) -> int:
	return max(0, round(normal(NETWORK_SIZES[edge_type])))

def add_network(graph: nx.Graph, edge_type: EdgeType, num: int):
	graph.add_edges_from([(num, (num, i)) for i in range(network_size_for_edge_type(edge_type))], edge_type=edge_type)

def create_graph() -> nx.Graph:
	graph = nx.Graph()
	for i in range(NUMBER_OF_LOCAL_WIRED_NETWORKS):
		add_network(graph, EdgeType.LOCAL_WIRED, i)
	for i in range(NUMBER_OF_LOCAL_WIRED_NETWORKS, NUMBER_OF_LOCAL_NETWORKS):
		add_network(graph, EdgeType.LOCAL_WIRELESS, i)
	for i in range(NUMBER_OF_USB_SHARING_NETWORKS):
		for router_node in sample(range(NUMBER_OF_LOCAL_NETWORKS), max(0, round(normal(NETWORK_SIZES[EdgeType.USB_SHARED]['NETWORKS'])))):
			child_nodes = len(list(graph.neighbors(router_node)))
			nodes = sample(range(child_nodes), max(0, min(round(normal(NETWORK_SIZES[EdgeType.USB_SHARED]['NODES_IN_NETWORK'])), child_nodes)))
			for node in nodes:
				graph.add_edge(f'person_{i}', (router_node, node), edge_type=EdgeType.USB_SHARED)
		for disconnected_computer in range(max(0, round(normal(NETWORK_SIZES[EdgeType.USB_SHARED]['DISCONNECTED'])))):
			graph.add_edge(f'person_{i}', f'disconnected_{disconnected_computer}', edge_type=EdgeType.USB_SHARED)
	for i in range(NUMBER_OF_LOCAL_NETWORKS):
		graph.add_edge(i, NUMBER_OF_LOCAL_NETWORKS)
	return graph