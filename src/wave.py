import networkx as nx
from random import random
from constants import *
from node import is_node_infected, set_node_infected, get_node_type, local_network_neighbors, get_usb_node_infection_limit, decrement_usb_node_infection_limit
from edge_type import EdgeType
from node_type import NodeType
from log import add_line_to_log

def should_infect_node_with_probability(probability: float) -> bool:
	return random() < probability

def node_type_is_not_router_or_main(graph: nx.Graph, node) -> bool:
	node_type = get_node_type(graph, node)
	return not (node_type == NodeType.ROUTER or node_type == NodeType.MAIN)

def new_wave(graph: nx.Graph) -> list:
	actions = []
	pending_windows_auto_update_infection_nodes = list(filter(lambda node: graph.node[node].get('pending_windows_auto_update_infection'), graph.node))
	for node in filter(lambda node: is_node_infected(graph, node), graph.nodes):
		node_type = get_node_type(graph, node)
		is_usb_node = node_type == NodeType.USB
		if is_usb_node and get_usb_node_infection_limit(graph, node) <= 0:
			continue
		for neighbor_node, edge_data in filter(
			lambda adjacency: not is_node_infected(graph, adjacency[0]),
			list(filter(
				lambda adjacency: node_type_is_not_router_or_main(graph, adjacency[0]),
				graph.adj[node].items()
			)) + (local_network_neighbors(graph, node) if node_type == NodeType.COMPUTER else [])
		):
			edge_type = edge_data['edge_type']
			def infect_neighbor_node(message: str) -> str:
				set_node_infected(graph, neighbor_node, True)
				return f'**`{neighbor_node}`** was infected by **`{node}`** using the **{message}**'
			if edge_type == EdgeType.LOCAL_WIRED:
				if should_infect_node_with_probability(PRINT_SPOOLER_TRANSMISSION_PROBABILITY):
					actions.append(infect_neighbor_node('print spooler vulnerability'))
				elif should_infect_node_with_probability(WINCC_TRANSMISSION_PROBABILITY):
					actions.append(infect_neighbor_node('WinCC vulnerability'))
				elif should_infect_node_with_probability(SMB_TRANSMISSION_PROBABILITY):
					actions.append(infect_neighbor_node('SMB vulnerability'))
				elif should_infect_node_with_probability(NETWORK_SHARES_TRANSMISSION_PROBABILITY):
					actions.append(infect_neighbor_node('network sharing vulnerability'))
			elif edge_type == EdgeType.LOCAL_WIRELESS:
				if should_infect_node_with_probability(NETWORK_SHARES_TRANSMISSION_PROBABILITY):
					actions.append(infect_neighbor_node('network sharing vulnerability'))
			elif edge_type == EdgeType.USB_SHARED or edge_type == EdgeType.USB_TO_PLC:
				did_infect_neighbor_node = False
				if should_infect_node_with_probability(USB_TRANSMISSION_PROBABILITY):
					actions.append(infect_neighbor_node('USB vulnerability'))
					did_infect_neighbor_node = True
				elif should_infect_node_with_probability(LNK_TRANSMISSION_PROBABILITY):
					actions.append(infect_neighbor_node('LNK vulnerability'))
					did_infect_neighbor_node = True
				elif should_infect_node_with_probability(AUTORUN_TRANSMISSION_PROBABILITY):
					actions.append(infect_neighbor_node('autorun vulnerability'))
					did_infect_neighbor_node = True
				if did_infect_neighbor_node and is_usb_node:
					decrement_usb_node_infection_limit(graph, node)
			elif edge_type == EdgeType.LOCAL_WIRED or edge_type == EdgeType.LOCAL_WIRELESS:
				if should_infect_node_with_probability(WINDOWS_AUTO_UPDATE_TRANSMISSION_PROBABILITY):
					graph.node[neighbor_node]['pending_windows_auto_update_infection'] = True
					actions.append(add_line_to_log(f'**`{neighbor_node}`** was given the **Windows auto update virus** by **`{node}`**'))
	for node in pending_windows_auto_update_infection_nodes:
		set_node_infected(graph, node, True)
		graph.node[node].pop('pending_windows_auto_update_infection')
		actions.append(add_line_to_log(f'**`{node}`** was infected by the **Windows auto update vulnerability**'))
	return actions