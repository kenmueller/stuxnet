import networkx as nx
from random import random
from constants import *
from node import is_node_infected, set_node_infected
from edge_type import EdgeType

def should_infect_node_with_probability(probability: float) -> bool:
	return random() < probability

def new_wave(graph: nx.Graph):
	edge_types = nx.get_edge_attributes(graph, 'edge_type')
	for node in filter(lambda node: is_node_infected(graph, node), graph.nodes):
		for neighbor_node, edge_data in graph.adj[node].items():
			edge_type = edge_data['edge_type']
			if edge_type == EdgeType.LOCAL_WIRED and (
				should_infect_node_with_probability(PRINT_SPOOLER_TRANSMISSION_PROBABILITY) or \
				should_infect_node_with_probability(WINCC_TRANSMISSION_PROBABILITY) or \
				should_infect_node_with_probability(SMB_TRANSMISSION_PROBABILITY) or \
				should_infect_node_with_probability(NETWORK_SHARES_TRANSMISSION_PROBABILITY)
			):
				set_node_infected(graph, neighbor_node, True)
			elif edge_type == EdgeType.LOCAL_WIRELESS and should_infect_node_with_probability(NETWORK_SHARES_TRANSMISSION_PROBABILITY):
				set_node_infected(graph, neighbor_node, True)
			elif edge_type == EdgeType.USB_SHARED and should_infect_node_with_probability(USB_TRANSMISSION_PROBABILITY):
				set_node_infected(graph, neighbor_node, True)