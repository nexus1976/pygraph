from enum import Enum


class TraversalType(Enum):
    DepthFirst = 0,
    BreadthFirst = 1

class Graph:

    Nodes = {}

    def __init__(self) -> None:
        pass