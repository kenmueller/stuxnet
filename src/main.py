import networkx as nx
import matplotlib.pyplot as plt
from constants import *
from create_graph import create_graph
from wave import new_wave
from node import is_node_infected, get_node_type
from log import add_line_to_log, write_log_file
from node_type import NodeType

INFECTED_NODE_COLOR = 'red'
NOT_INFECTED_NODE_COLOR = 'green'

def draw_graph(graph: nx.Graph, colors: list = None, **kwargs):
	nx.draw(graph, node_color=colors, with_labels=True)
	plt.show(**kwargs)

def get_graph_colors(graph: nx.Graph):
	return [INFECTED_NODE_COLOR if is_node_infected(graph, node) else NOT_INFECTED_NODE_COLOR for node in graph.nodes]

def node_total_attributes(graph: nx.Graph) -> dict:
	filter_for_node_type = lambda node_type: list(filter(lambda node: get_node_type(graph, node) == node_type, graph.node))
	return {
		NodeType.COMPUTER: len(filter_for_node_type(NodeType.COMPUTER)),
		NodeType.DISCONNECTED_COMPUTER: len(filter_for_node_type(NodeType.DISCONNECTED_COMPUTER)),
		NodeType.USB: len(filter_for_node_type(NodeType.USB)),
		'total': len(graph.node)
	}

def node_infected_attributes(graph: nx.Graph) -> dict:
	infected_nodes = list(filter(lambda node: is_node_infected(graph, node), graph.node))
	number_of_infected_nodes = len(infected_nodes)
	filter_for_node_type = lambda node_type: list(filter(lambda node: get_node_type(graph, node) == node_type, infected_nodes))
	return {
		NodeType.COMPUTER: len(filter_for_node_type(NodeType.COMPUTER)),
		NodeType.DISCONNECTED_COMPUTER: len(filter_for_node_type(NodeType.DISCONNECTED_COMPUTER)),
		NodeType.USB: len(filter_for_node_type(NodeType.USB)),
		'total': number_of_infected_nodes,
		'healthy': len(graph.node) - number_of_infected_nodes
	}

if __name__ == '__main__':
	graph = create_graph()
	old_infected_attributes = node_infected_attributes(graph)
	total_attributes = node_total_attributes(graph)
	log = f'# **Initial**\n\n## **{old_infected_attributes[NodeType.USB]}/{total_attributes[NodeType.USB]} USB nodes infected**\n'
	for wave in range(INFECTION_DURATION // WAVE_DURATION):
		log = add_line_to_log(log, f'\n# **Wave {wave + 1}**\n\n## **Actions**', extra_newline=True)
		log = new_wave(graph, log)
		new_infected_attributes = node_infected_attributes(graph)
		log = add_line_to_log(log, f'\n## **Summary**', extra_newline=True)
		log = add_line_to_log(log, f'- **Computer nodes infected:** +{new_infected_attributes[NodeType.COMPUTER] - old_infected_attributes[NodeType.COMPUTER]}, {new_infected_attributes[NodeType.COMPUTER]}/{total_attributes[NodeType.COMPUTER]} total')
		log = add_line_to_log(log, f'- **Disconnected computer nodes infected:** +{new_infected_attributes[NodeType.DISCONNECTED_COMPUTER] - old_infected_attributes[NodeType.DISCONNECTED_COMPUTER]}, {new_infected_attributes[NodeType.DISCONNECTED_COMPUTER]}/{total_attributes[NodeType.DISCONNECTED_COMPUTER]} total')
		log = add_line_to_log(log, f'- **USB nodes infected:** +{new_infected_attributes[NodeType.USB] - old_infected_attributes[NodeType.USB]}, {new_infected_attributes[NodeType.USB]}/{total_attributes[NodeType.USB]} total')
		log = add_line_to_log(log, f'- **Overall infected:** +{new_infected_attributes["total"] - old_infected_attributes["total"]}, {new_infected_attributes["total"]}/{total_attributes["total"]} total')
		log = add_line_to_log(log, f'- **Overall healthy:** {new_infected_attributes["healthy"] - old_infected_attributes["healthy"]}, {new_infected_attributes["healthy"]}/{total_attributes["total"]} total')
		old_infected_attributes = new_infected_attributes
	write_log_file(log)
	draw_graph(graph, get_graph_colors(graph))