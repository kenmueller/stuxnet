import networkx as nx
from node_type import NodeType

def is_node_infected(graph: nx.Graph, node) -> bool:
	return graph.node[node].get('infected', False)

def set_node_infected(graph: nx.Graph, node, infected: bool):
	if infected:
		graph.node[node]['infected'] = True
	else:
		graph.node[node].pop('infected')

def get_node_type(graph: nx.Graph, node) -> NodeType:
	return graph.node[node]['node_type']

def set_node_type(graph: nx.Graph, node, node_type: NodeType):
	graph.node[node]['node_type'] = node_type

def local_network_neighbors(graph: nx.Graph, node) -> list:
	return list(filter(
		lambda adjacency: get_node_type(graph, adjacency[0]) == NodeType.COMPUTER,
		graph[list(filter(lambda neighbor_node: get_node_type(graph, neighbor_node) == NodeType.ROUTER, graph.neighbors(node)))[0]].items()
	))

def get_usb_node_infection_limit(graph: nx.Graph, node) -> int:
	return graph.node[node]['infection_limit']

def decrement_usb_node_infection_limit(graph: nx.Graph, node):
	graph.node[node]['infection_limit'] -= 1