from edge_type import EdgeType

# Network structure

# Network sizes for edge types
NETWORK_SIZES = {
	EdgeType.LOCAL_WIRED: 6.5,
	EdgeType.LOCAL_WIRELESS: 8.1,
	EdgeType.USB_SHARED: {
		'NETWORKS': 2,
		'NODES_IN_NETWORK': 2,
		'DISCONNECTED': 1
	}
}

# Total number of local wired networks
NUMBER_OF_LOCAL_WIRED_NETWORKS = 10

# Total number of local wireless networks
NUMBER_OF_LOCAL_WIRELESS_NETWORKS = 20

# Total number of USB sharing networks
NUMBER_OF_USB_SHARING_NETWORKS = 30

# Transmission probabilities

# The probability, for each wave, that an infected computer will infect its neighbor via USB
USB_TRANSMISSION_PROBABILITY = 0.1

# The probability, for each wave, that an infected computer will infect its neighbor via LNK vulnerability
LNK_TRANSMISSION_PROBABILITY = 0.5

# The probability, for each wave, that an infected computer will infect its neighbor via autorun vulnerability
AUTORUN_TRANSMISSION_PROBABILITY = 0.5

# The probability, for each wave, that an infected computer will infect its neighbor via print spooler vulnerability
PRINT_SPOOLER_TRANSMISSION_PROBABILITY = 0.5

# The probability, for each wave, that an infected computer will infect its neighbor via WinCC
WINCC_TRANSMISSION_PROBABILITY = 0.5

# The probability, for each wave, that an infected computer will infect its neighbor via a network share
NETWORK_SHARES_TRANSMISSION_PROBABILITY = 0.5

# The probability, for each wave, that an infected computer will infect its neighbor via SMB
SMB_TRANSMISSION_PROBABILITY = 0.5

# The probability, for each wave, that a given computer will get infected from a windows auto update
WINDOWS_AUTO_UPDATE_TRANSMISSION_PROBABILITY = 0.5

# Limits

# The number of milliseconds a wave is
WAVE_DURATION = 86400000

# The number of milliseconds until stuxnet self destructs
INFECTION_DURATION = 94608000000

# The number of computers stuxnet can infect before it turns itself off
INFECTION_LIMIT = 3