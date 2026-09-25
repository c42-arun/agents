from enum import Enum

class LsRequester(str, Enum):
    Broker = "Broker",
    Client = "Client",

