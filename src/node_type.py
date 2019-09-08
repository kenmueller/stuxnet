from enum import Enum, unique, auto

@unique
class NodeType(Enum):
	MAIN = auto()
	ROUTER = auto()
	COMPUTER = auto()
	DISCONNECTED_COMPUTER = auto()
	USB = auto()
	PLC = auto()