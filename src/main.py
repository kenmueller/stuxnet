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

def get_graph_colors(graph: nx.Graph) -> list:
	return [INFECTED_NODE_COLOR if is_node_infected(graph, node) else NOT_INFECTED_NODE_COLOR for node in graph.nodes]

def node_total_attributes(graph: nx.Graph) -> dict:
	filter_for_node_type = lambda node_type: list(filter(lambda node: get_node_type(graph, node) == node_type, graph.node))
	return {
		NodeType.COMPUTER: len(filter_for_node_type(NodeType.COMPUTER)),
		NodeType.DISCONNECTED_COMPUTER: len(filter_for_node_type(NodeType.DISCONNECTED_COMPUTER)),
		NodeType.USB: len(filter_for_node_type(NodeType.USB)),
		NodeType.PLC: len(filter_for_node_type(NodeType.PLC)),
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
		NodeType.PLC: len(filter_for_node_type(NodeType.PLC)),
		'total': number_of_infected_nodes,
		'healthy': len(graph.node) - number_of_infected_nodes
	}

if __name__ == '__main__':
	graph = create_graph()
	old_infected_attributes = node_infected_attributes(graph)
	total_attributes = node_total_attributes(graph)
	log = f'# **Initial**\n\n## **{old_infected_attributes[NodeType.USB]}/{total_attributes[NodeType.USB]} USB nodes infected**\n'
	number_of_waves = int(INFECTION_DURATION // WAVE_DURATION)
	for wave in range(number_of_waves):
		print(f'Wave {wave + 1}/{number_of_waves}')
		log = add_line_to_log(log, f'\n<div id="wave-{wave + 1}"></div>\n\n# **Wave {wave + 1}**\n\n**[Summary](#wave-{wave + 1}-summary){"" if wave == number_of_waves - 1 else f" • [Next](#wave-{wave + 2})"}**', extra_newline=True)
		actions = new_wave(graph)
		if len(actions):
			log = add_line_to_log(log, '## **Actions**', extra_newline=True)
			for action in actions:
				log = add_line_to_log(log, f'1. {action}')
			log = add_line_to_log(log)
		new_infected_attributes = node_infected_attributes(graph)
		log = add_line_to_log(log, f'<div id="wave-{wave + 1}-summary"></div>\n\n## **Wave {wave + 1} summary**', extra_newline=True)
		log = add_line_to_log(log, f'- **Computer nodes infected:** `+{new_infected_attributes[NodeType.COMPUTER] - old_infected_attributes[NodeType.COMPUTER]}`, {new_infected_attributes[NodeType.COMPUTER]}/{total_attributes[NodeType.COMPUTER]} total')
		log = add_line_to_log(log, f'- **Disconnected computer nodes infected:** `+{new_infected_attributes[NodeType.DISCONNECTED_COMPUTER] - old_infected_attributes[NodeType.DISCONNECTED_COMPUTER]}`, {new_infected_attributes[NodeType.DISCONNECTED_COMPUTER]}/{total_attributes[NodeType.DISCONNECTED_COMPUTER]} total')
		log = add_line_to_log(log, f'- **USB nodes infected:** `+{new_infected_attributes[NodeType.USB] - old_infected_attributes[NodeType.USB]}`, {new_infected_attributes[NodeType.USB]}/{total_attributes[NodeType.USB]} total')
		log = add_line_to_log(log, f'- **PLC nodes infected:** `+{new_infected_attributes[NodeType.PLC] - old_infected_attributes[NodeType.PLC]}`, {new_infected_attributes[NodeType.PLC]}/{total_attributes[NodeType.PLC]} total')
		log = add_line_to_log(log, f'- **Overall infected:** `+{new_infected_attributes["total"] - old_infected_attributes["total"]}`, {new_infected_attributes["total"]}/{total_attributes["total"]} total')
		log = add_line_to_log(log, f'- **Overall healthy:** `-{abs(new_infected_attributes["healthy"] - old_infected_attributes["healthy"])}`, {new_infected_attributes["healthy"]}/{total_attributes["total"]} total')
		old_infected_attributes = new_infected_attributes
	write_log_file(log)
	if SHOULD_DRAW_GRAPH:
		draw_graph(graph, get_graph_colors(graph))