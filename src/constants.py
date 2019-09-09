from edge_type import EdgeType

# Network structure

# Network sizes for edge types
NETWORK_SIZES = {
	# How many computers there are inside of a local wired network
	EdgeType.LOCAL_WIRED: 10,

	# How many computers there are inside of a local wireless network
	EdgeType.LOCAL_WIRELESS: 15,

	EdgeType.USB_SHARED: {
		# How many different networks a single USB drive should connect to
		'NUMBER_OF_NETWORKS': 3,

		# How many nodes in each network a single USB drive should connect to
		'NODES_IN_NETWORK': 4,

		# How many disconnected computers a single USB drive should connect to
		'NUMBER_OF_DISCONNECTED_COMPUTERS': 1
	}
}

# Total number of local wired networks
NUMBER_OF_LOCAL_WIRED_NETWORKS = 3000

# Total number of local wireless networks
NUMBER_OF_LOCAL_WIRELESS_NETWORKS = 5000

# Total number of USB sharing networks
NUMBER_OF_USB_SHARING_NETWORKS = 400

# Total number of PLCs
NUMBER_OF_PLC_NODES = 10000

# Transmission probabilities

# USB edge type

# The probability, for each wave, that an infected computer will infect its neighbor via USB
USB_TRANSMISSION_PROBABILITY = 0.01

# The probability, for each wave, that an infected computer will infect its neighbor via LNK vulnerability
LNK_TRANSMISSION_PROBABILITY = 0.1

# The probability, for each wave, that an infected computer will infect its neighbor via autorun vulnerability
AUTORUN_TRANSMISSION_PROBABILITY = 0.1

# Wired local network edge type

# The probability, for each wave, that an infected computer will infect its neighbor via print spooler vulnerability
PRINT_SPOOLER_TRANSMISSION_PROBABILITY = 0.1

# The probability, for each wave, that an infected computer will infect its neighbor via WinCC
WINCC_TRANSMISSION_PROBABILITY = 0.1

# The probability, for each wave, that an infected computer will infect its neighbor via SMB
SMB_TRANSMISSION_PROBABILITY = 0.1

# Wired and wireless local network edge type

# The probability, for each wave, that an infected computer will infect its neighbor via a network share
NETWORK_SHARES_TRANSMISSION_PROBABILITY = 0.1

# The probability, for each wave, that a given computer will get infected from a windows auto update
WINDOWS_AUTO_UPDATE_TRANSMISSION_PROBABILITY = 0.1

# Limits

# The number of milliseconds a wave is
WAVE_DURATION = 86400000

# The number of milliseconds until stuxnet self destructs
INFECTION_DURATION = 94608000000

# The number of computers a USB can infect before it self destructs
INFECTION_LIMIT = 3

# Number of initial USB nodes infected. Should be less than the number of USB sharing networks
NUMBER_OF_INITIAL_USB_NODES_INFECTED = 10

# Should draw the graph at the end
SHOULD_DRAW_GRAPH = False