import networkx as nx
from node import is_node_infected, set_node_infected
from edge_type import EdgeType

def new_wave(graph: nx.Graph):
	edge_types = nx.get_edge_attributes(graph, 'edge_type')
	for node in filter(lambda node: is_node_infected(graph, node), graph.nodes):
		for neighbor_node, edge_data in graph.adj[node].items():
			edge_type = edge_data['edge_type']
			if edge_type == EdgeType.LOCAL_WIRED:
				pass
			elif edge_type == EdgeType.LOCAL_WIRELESS:
				pass
			elif edge_type == EdgeType.USB_SHARED:
				pass
			elif edge_type == EdgeType.MAIN_TO_ROUTER:
				pass