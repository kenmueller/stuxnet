import networkx as nx
import matplotlib.pyplot as plt
from create_graph import create_graph
from edge_type import EdgeType

if __name__ == '__main__':
	nx.draw(create_graph(), with_labels=True)
	plt.show()