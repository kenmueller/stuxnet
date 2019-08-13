from edge_type import EdgeType

# Network structure

NETWORK_SIZES = {
	EdgeType.LOCAL_WIRED: 6.5,
	EdgeType.LOCAL_WIRELESS: 8.1,
	EdgeType.USB_SHARED: 4.1
}

NUMBER_OF_LOCAL_WIRED_NETWORKS = 10

NUMBER_OF_LOCAL_WIRELESS_NETWORKS = 20

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