# Network structure

# Average number of computers in a local network
AVERAGE_LOCAL_NETWORK_SIZE = 14

# Average number of computers a single usb drive will be plugged in to
AVERAGE_USB_DRIVE_SHARING_NETWORK_SIZE = 5

# Average number of local networks contained in a single "big" network
AVERAGE_NUMBER_OF_LOCAL_NETWORKS_IN_BIG_NETWORK = 3

# Total number of big networks
NUMBER_OF_BIG_NETWORKS = 25

# Infection rate

# The probability, for each wave, that if you're a neighbor of an infected computer, you will be infected as well
USB_TRANSMISSION_PROBABILITY = 0.1

# The probability, for each wave, that if you're on the same local network as an infected computer, you will be infected as well
LOCAL_NETWORK_TRANSMISSION_PROBABILITY = 0.2

# The probability, for each wave, that you will get infected with Stuxnet's Windows autoupdate hack
WINDOWS_AUTO_UPDATE_TRANSMISSION_PROBABILITY = .1