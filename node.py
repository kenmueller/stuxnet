import networkx as nx

def is_node_infected(graph: nx.Graph, node) -> bool:
	return graph.nodes[node].get('infected', False)