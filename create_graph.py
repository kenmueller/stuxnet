import networkx as nx
from numpy.random import normal
from random import sample
from constants import *
from edge_type import EdgeType

NUMBER_OF_LOCAL_NETWORKS = NUMBER_OF_LOCAL_WIRED_NETWORKS + NUMBER_OF_LOCAL_WIRELESS_NETWORKS
USB_SHARED_NETWORK_SIZES = NETWORK_SIZES[EdgeType.USB_SHARED]

def bound_normal(value: float) -> int:
	"""Returns a positive `int` using a normal curve"""
	return max(0, round(normal(value)))

def network_size_for_edge_type(edge_type: EdgeType) -> int:
	"""Gets the network size for an edge type as a positive `int` from a normal curve"""
	return bound_normal(NETWORK_SIZES[edge_type])

def add_computer_nodes(graph: nx.Graph, edge_type: EdgeType, router_node: int):
	"""Adds computer nodes from a router node to a graph"""
	# Add edges from the router node to all of the computer nodes labeled (router node, computer node)
	graph.add_edges_from([(router_node, (router_node, computer_node)) for computer_node in range(network_size_for_edge_type(edge_type))], edge_type=edge_type)

def create_graph() -> nx.Graph:
	"""Creates a graph for Stuxnet to infect"""
	# Create an empty graph
	graph = nx.Graph()

	# Add router nodes and computer nodes for all the wired networks
	for router_node in range(NUMBER_OF_LOCAL_WIRED_NETWORKS):
		add_computer_nodes(graph, EdgeType.LOCAL_WIRED, router_node)

	# Add router nodes and computer nodes for all the wireless networks
	for router_node in range(NUMBER_OF_LOCAL_WIRED_NETWORKS, NUMBER_OF_LOCAL_NETWORKS):
		add_computer_nodes(graph, EdgeType.LOCAL_WIRELESS, router_node)

	# Add USB sharing networks
	for usb_node in range(NUMBER_OF_USB_SHARING_NETWORKS):
		# The label that the USB node should have on the graph
		usb_node_label = f'usb-{usb_node}'

		# Get how many different networks a USB drive should infect, and then take the normal and making sure it's less
		# than the total number of networks. This retrieves all the parent router nodes of the computers that the USB drive
		# will infect.
		for router_node in sample(range(NUMBER_OF_LOCAL_NETWORKS), bound_normal(USB_SHARED_NETWORK_SIZES['NUMBER_OF_NETWORKS'])):
			# Get the number of computer nodes this router node connects to
			number_of_computer_nodes = len(list(graph.neighbors(router_node)))

			# Get the number of nodes a USB drive should infect in a single network, normalize it, make sure it's positive,
			# and also make sure it's less than the actual amount of computer nodes in the current network. Then, take a
			# sample of all the computer nodes in the current network using that number.
			for computer_node in sample(range(number_of_computer_nodes), min(bound_normal(USB_SHARED_NETWORK_SIZES['NODES_IN_NETWORK']), number_of_computer_nodes)):
				# Add an edge between the USB node and the computer node with an edge type of USB_SHARED
				graph.add_edge(usb_node_label, (router_node, computer_node), edge_type=EdgeType.USB_SHARED)

		# Get the number of disconnected computers a USB drive should infect, normalize it, and make sure it's positive
		for disconnected_computer_node in range(bound_normal(USB_SHARED_NETWORK_SIZES['NUMBER_OF_DISCONNECTED_COMPUTERS'])):
			# Add an edge with an edge type of USB_SHARED between the USB node and the disconnected computer, creating a
			# new disconnected computer if needed. 
			graph.add_edge(usb_node_label, f'disconnected-{disconnected_computer_node}', edge_type=EdgeType.USB_SHARED)

	# Connect all the router nodes to a singular node in the middle of the graph
	for router_node in range(NUMBER_OF_LOCAL_NETWORKS):
		graph.add_edge(router_node, NUMBER_OF_LOCAL_NETWORKS)

	return graph