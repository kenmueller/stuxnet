import networkx as nx
from random import random
from constants import *
from node import is_node_infected, set_node_infected, get_node_type, local_network_neighbors
from edge_type import EdgeType
from node_type import NodeType

def should_infect_node_with_probability(probability: float) -> bool:
	return random() < probability

def node_type_is_not_router_or_main(graph: nx.Graph, node) -> bool:
	node_type = get_node_type(graph, node)
	return not (node_type == NodeType.ROUTER or node_type == NodeType.MAIN)

def new_wave(graph: nx.Graph): 
	pending_windows_auto_update_infection_nodes = list(filter(lambda node: graph.node[node].get('pending_windows_auto_update_infection'), graph.node))
	for node in filter(lambda node: is_node_infected(graph, node), graph.nodes):
		for neighbor_node, edge_data in list(filter(lambda adjacency: node_type_is_not_router_or_main(graph, adjacency[0]), graph.adj[node].items())) + (local_network_neighbors(graph, node) if get_node_type(graph, node) == NodeType.COMPUTER else []):
			edge_type = edge_data['edge_type']
			infect_neighbor_node = lambda: set_node_infected(graph, neighbor_node, True)
			if edge_type == EdgeType.LOCAL_WIRED and (
				should_infect_node_with_probability(PRINT_SPOOLER_TRANSMISSION_PROBABILITY) or \
				should_infect_node_with_probability(WINCC_TRANSMISSION_PROBABILITY) or \
				should_infect_node_with_probability(SMB_TRANSMISSION_PROBABILITY) or \
				should_infect_node_with_probability(NETWORK_SHARES_TRANSMISSION_PROBABILITY)
			):
				infect_neighbor_node()
			elif edge_type == EdgeType.LOCAL_WIRELESS and should_infect_node_with_probability(NETWORK_SHARES_TRANSMISSION_PROBABILITY):
				infect_neighbor_node()
			elif edge_type == EdgeType.USB_SHARED and should_infect_node_with_probability(USB_TRANSMISSION_PROBABILITY):
				infect_neighbor_node()
			elif (edge_type == EdgeType.LOCAL_WIRED or edge_type == EdgeType.LOCAL_WIRELESS) and should_infect_node_with_probability(WINDOWS_AUTO_UPDATE_TRANSMISSION_PROBABILITY):
				graph.node[neighbor_node]['pending_windows_auto_update_infection'] = True
	for node in pending_windows_auto_update_infection_nodes:
		set_node_infected(graph, node, True)
		graph.node[node].pop('pending_windows_auto_update_infection')