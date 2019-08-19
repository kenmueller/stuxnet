import networkx as nx
from node_type import NodeType

def is_node_infected(graph: nx.Graph, node) -> bool:
	return graph.node[node].get('infected', False)

def set_node_infected(graph: nx.Graph, node, infected: bool):
	graph.node[node]['infected'] = infected

def get_node_type(graph: nx.Graph, node) -> NodeType:
	return graph.node[node]['node_type']

def set_node_type(graph: nx.Graph, node, node_type: NodeType):
	graph.node[node]['node_type'] = node_type

def local_network_neighbors(graph: nx.Graph, node):
	return list(filter(
		lambda adjacency: get_node_type(graph, adjacency[0]) == NodeType.COMPUTER,
		graph[list(filter(lambda neighbor_node: get_node_type(graph, neighbor_node) == NodeType.ROUTER, graph.neighbors(node)))[0]].items()
	))