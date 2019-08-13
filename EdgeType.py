from enum import Enum, unique, auto

@unique
class EdgeType(Enum):
	LOCAL_WIRED = auto()
	LOCAL_WIRELESS = auto()
	USB_SHARED = auto()