import networkx as nx
from numpy.random import normal
from random import sample
from constants import *
from edge_type import EdgeType

NUMBER_OF_LOCAL_NETWORKS = NUMBER_OF_LOCAL_WIRED_NETWORKS + NUMBER_OF_LOCAL_WIRELESS_NETWORKS
USB_SHARED_NETWORK_SIZES = NETWORK_SIZES[EdgeType.USB_SHARED]

def bound_normal(value: float) -> int:
	return max(0, round(normal(value)))

def network_size_for_edge_type(edge_type: EdgeType) -> int:
	return bound_normal(NETWORK_SIZES[edge_type])

def add_network(graph: nx.Graph, edge_type: EdgeType, parent_node: int):
	graph.add_edges_from([(parent_node, (parent_node, child_node)) for child_node in range(network_size_for_edge_type(edge_type))], edge_type=edge_type)

def create_graph() -> nx.Graph:
	graph = nx.Graph()
	for wired_network in range(NUMBER_OF_LOCAL_WIRED_NETWORKS):
		add_network(graph, EdgeType.LOCAL_WIRED, wired_network)
	for wireless_network in range(NUMBER_OF_LOCAL_WIRED_NETWORKS, NUMBER_OF_LOCAL_NETWORKS):
		add_network(graph, EdgeType.LOCAL_WIRELESS, wireless_network)
	for usb_sharing_network in range(NUMBER_OF_USB_SHARING_NETWORKS):
		for router_node in sample(range(NUMBER_OF_LOCAL_NETWORKS), bound_normal(USB_SHARED_NETWORK_SIZES['NETWORKS'])):
			number_of_child_nodes = len(list(graph.neighbors(router_node)))
			for child_node in sample(range(number_of_child_nodes), min(bound_normal(USB_SHARED_NETWORK_SIZES['NODES_IN_NETWORK']), number_of_child_nodes)):
				graph.add_edge(f'person-{usb_sharing_network}', (router_node, child_node), edge_type=EdgeType.USB_SHARED)
		for disconnected_computer in range(bound_normal(USB_SHARED_NETWORK_SIZES['DISCONNECTED'])):
			graph.add_edge(f'person-{usb_sharing_network}', f'disconnected-{disconnected_computer}', edge_type=EdgeType.USB_SHARED)
	for router_node in range(NUMBER_OF_LOCAL_NETWORKS):
		graph.add_edge(router_node, NUMBER_OF_LOCAL_NETWORKS)
	return graph