from enum import Enum, auto


class MachineState(Enum):
    IDLE = auto()
    WAITING_FOR_PAYMENT = auto()
    PAYMENT_RECEIVED = auto()
    DISPENSING = auto()
    OUT_OF_ORDER = auto()