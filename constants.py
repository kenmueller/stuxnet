import numpy.random as random

def __value_from_normal_curve(average, min = None):
	normal = random.normal(average)
	return normal if min is None else max(min, normal)

# Network structure

# Total number of big networks
NUMBER_OF_BIG_NETWORKS = 25

def USB_DRIVE_SHARING_NETWORK_SIZE():
	"""Number of computers a single usb drive will be plugged in to"""
	return __value_from_normal_curve(5, 0)

def LOCAL_WIRED_NETWORK_SIZE():
	"""Number of computers in a single wired network (Ethernet)"""
	return __value_from_normal_curve(10, 0)

def LOCAL_WIRELESS_NETWORK_SIZE():
	"""Number of computers in a single wireless network"""
	return __value_from_normal_curve(30, 0)

def NUMBER_OF_LOCAL_NETWORKS_IN_BIG_NETWORK():
	"""Number of local networks contained in a single "big" network"""
	return __value_from_normal_curve(3, 0)

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

# The number of milliseconds a wave corresponds to
WAVE_LENGTH = 86400000

# The number of computers stuxnet can infect before it turns itself off
INFECTION_LIMIT = 3

# The number of milliseconds until stuxnet self destructs
INFECTION_DURATION = 94608000000