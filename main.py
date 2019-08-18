import networkx as nx
import matplotlib.pyplot as plt
from create_graph import create_graph
from wave import new_wave

def draw_graph(graph: nx.Graph, **kwargs):
	nx.draw(graph, with_labels=True)
	plt.show(**kwargs)

if __name__ == '__main__':
	graph = create_graph()
	draw_graph(graph, block=False)
	# TODO: Create waves and display data
	plt.show()