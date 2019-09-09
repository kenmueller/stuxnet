import networkx as nx
from numpy.random import normal
from random import sample, choice
from constants import *
from edge_type import EdgeType
from node_type import NodeType
from node import set_node_infected, get_node_type, set_node_type

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
	# Get the network size for the edge type and create a range
	network_size_range = range(network_size_for_edge_type(edge_type))

	# Add edges from the router node to all of the computer nodes labeled (router node, computer node)
	graph.add_edges_from([(router_node, (router_node, computer_node)) for computer_node in network_size_range], edge_type=edge_type)

	# Set node attributes for all the computer nodes
	for computer_node in network_size_range:
		set_node_type(graph, (router_node, computer_node), NodeType.COMPUTER)

def set_default_infection_limit(graph: nx.Graph, usb_node: str):
	"""Sets the default infection limit for a USB node"""
	graph.node[usb_node]['infection_limit'] = INFECTION_LIMIT

def get_usb_nodes(graph: nx.Graph) -> list:
	"""Gets all the USB nodes in a graph"""
	return [f'usb-{usb_node}' for usb_node in range(NUMBER_OF_USB_SHARING_NETWORKS)]

def add_plc_nodes(graph: nx.Graph):
	"""Adds all the PLC nodes in a graph"""
	# Get all the USB nodes
	usb_nodes = get_usb_nodes(graph)

	# Get the range of PLC nodes
	plc_node_range = range(NUMBER_OF_PLC_NODES)

	# Add all the edges between a USB node and a new PLC node
	graph.add_edges_from([(choice(usb_nodes), f'plc-{i}') for i in plc_node_range], edge_type=EdgeType.USB_TO_PLC)

	# Set the node type for all the new PLC nodes
	for i in plc_node_range:
		set_node_type(graph, f'plc-{i}', NodeType.PLC)

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
			# sample of all the computer nodes in the current network using that number. Add an edge between the USB node
			# and the computer node with an edge type of USB_SHARED.
			graph.add_edges_from([
				(usb_node_label, (router_node, computer_node))
				for computer_node in sample(
					range(number_of_computer_nodes),
					min(bound_normal(USB_SHARED_NETWORK_SIZES['NODES_IN_NETWORK']), number_of_computer_nodes)
				)
			], edge_type=EdgeType.USB_SHARED)

		# Get the number of disconnected computers a USB drive should infect, normalize it, and make sure it's positive
		for disconnected_computer_node in range(bound_normal(USB_SHARED_NETWORK_SIZES['NUMBER_OF_DISCONNECTED_COMPUTERS'])):
			# The label that the disconnected computer node should have on the graph
			disconnected_computer_node_label = f'disconnected-{disconnected_computer_node}'

			# Add an edge with an edge type of USB_SHARED between the USB node and the disconnected computer, creating a
			# new disconnected computer if needed.
			graph.add_edge(usb_node_label, disconnected_computer_node_label, edge_type=EdgeType.USB_SHARED)

			# Set the node type of the new disconnected computer node
			set_node_type(graph, disconnected_computer_node_label, NodeType.DISCONNECTED_COMPUTER)

		# Get a sample of all the valid nodes for the USB node to connect to if it has less than 2 neighbors
		sample_valid_nodes = lambda count: sample(list(filter(lambda node: graph.node.get(node) and get_node_type(graph, node) != NodeType.ROUTER, graph.nodes)), count)

		# Check if the USB node exists
		if graph.adj.get(usb_node_label):
			# The USB node exists, now we're checking if it only has 1 neighbor
			if len(graph[usb_node_label]) == 1:
				# We now add the other neighbor to the USB node since it previously only had 1 neighbor
				graph.add_edge(usb_node_label, sample_valid_nodes(1)[0], edge_type=EdgeType.USB_SHARED)
		else:
			# The USB node doesn't exist, so we add 2 connections to other nodes
			graph.add_edges_from([(usb_node_label, node) for node in sample_valid_nodes(2)], edge_type=EdgeType.USB_SHARED)

		# Set the node type for the USB node
		set_node_type(graph, usb_node_label, NodeType.USB)

		# Set the default infection limit for the USB node
		set_default_infection_limit(graph, usb_node_label)

	# Get a sample of all the USB nodes, and infect all the nodes that should be initially infected
	for usb_node in sample(range(NUMBER_OF_USB_SHARING_NETWORKS), NUMBER_OF_INITIAL_USB_NODES_INFECTED):
		set_node_infected(graph, f'usb-{usb_node}', True)

	# Connect all the router nodes to a singular node in the middle of the graph
	for router_node in range(NUMBER_OF_LOCAL_NETWORKS):
		graph.add_edge(router_node, NUMBER_OF_LOCAL_NETWORKS, edge_type=EdgeType.MAIN_TO_ROUTER)
		set_node_type(graph, router_node, NodeType.ROUTER)

	# Set the node type for the main node
	set_node_type(graph, NUMBER_OF_LOCAL_NETWORKS, NodeType.MAIN)

	# Add PLCs to the graph
	add_plc_nodes(graph)

	return graph