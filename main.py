import networkx as nx
import matplotlib.pyplot as plt
from constants import *
from create_graph import create_graph
from wave import new_wave
from node import is_node_infected

INFECTED_NODE_COLOR = 'red'
NOT_INFECTED_NODE_COLOR = 'green'

def draw_graph(graph: nx.Graph, colors: [str] = None, **kwargs):
	nx.draw(graph, node_color=colors, with_labels=True)
	plt.show(**kwargs)

def get_graph_colors(graph: nx.Graph):
	return [INFECTED_NODE_COLOR if is_node_infected(graph, node) else NOT_INFECTED_NODE_COLOR for node in graph.nodes]

def number_of_infected_nodes(graph: nx.Graph) -> int:
	return len(list(filter(lambda node: is_node_infected(graph, node), graph.nodes)))

def number_of_infected_nodes_wave_description(graph: nx.Graph, wave: int) -> str:
	infected_nodes = number_of_infected_nodes(graph)
	return f'Wave {wave}: {infected_nodes} node{"" if infected_nodes == 1 else "s"} infected'

if __name__ == '__main__':
	graph = create_graph()
	print(number_of_infected_nodes_wave_description(graph, 0))
	for wave in range(INFECTION_DURATION // WAVE_DURATION):
		new_wave(graph)
		print(number_of_infected_nodes_wave_description(graph, wave + 1))
	draw_graph(graph, get_graph_colors(graph))