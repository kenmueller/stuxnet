import networkx as nx
import matplotlib.pyplot as plt
from create_graph import create_graph

if __name__ == '__main__':
	nx.draw(create_graph(), with_labels=True)
	plt.show()