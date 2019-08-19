import networkx as nx
from node_type import NodeType

def is_node_infected(graph: nx.Graph, node) -> bool:
	return graph.nodes[node].get('infected', False)

def set_node_infected(graph: nx.Graph, node, infected: bool):
	graph.node[node]['infected'] = infected

def get_node_type(graph: nx.Graph, node) -> NodeType:
	return graph.node[node]['node_type']

def set_node_type(graph: nx.Graph, node, node_type: NodeType):
	graph.node[node]['node_type'] = node_type