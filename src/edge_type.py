from enum import Enum, unique, auto

@unique
class EdgeType(Enum):
	LOCAL_WIRED = auto()
	LOCAL_WIRELESS = auto()
	USB_SHARED = auto()
	USB_TO_PLC = auto()
	MAIN_TO_ROUTER = auto()