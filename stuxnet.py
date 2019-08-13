import networkx as nx
import matplotlib.pyplot as plt
from create_graph import create_graph

nx.draw(create_graph(), with_labels=True)
plt.show()