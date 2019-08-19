import networkx as nx

def is_node_infected(graph: nx.Graph, node) -> bool:
	return graph.nodes[node].get('infected', False)

def set_node_infected(graph: nx.Graph, node, infected: bool):
	nx.set_node_attributes(graph, { node: { 'infected': infected } })