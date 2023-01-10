from typing import Dict
from graphNode import GraphNode

class GraphNode:
    Value = 0
    Neighbors: Dict[int, GraphNode] = {}

    def __init__(self, value) -> None:
        self.Value = value

    def __str__(self) -> str:
        strTemplate = "GraphNode Value: {0} | Neighbors Count: {1}"
        return strTemplate.format(self.Value, len(self.Neighbors))
    
    @classmethod
    def AddNeighbor(self, neighbor: GraphNode) -> bool:
        if neighbor is not None and type(neighbor) is GraphNode:
            if neighbor.Value not in self.Neighbors:
                self.Neighbors[neighbor.Value] = neighbor
                return True
        return False
    
    @classmethod
    def RemoveNeighbor(self, neighbor: GraphNode) -> bool:
        if neighbor is not None and type(neighbor) is GraphNode:
            if neighbor.Value in self.Neighbors:
                self.Neighbors.pop(neighbor.Value)
                return True
        return False
    
    @classmethod
    def RemoveNeighbor(self, value: int) -> bool:
        if value is not None and type(value) is int:
            if value in self.Neighbors:
                self.Neighbors.pop(value)
                return True
        return False

    @classmethod
    def HasNeighbor(self, neighbor: GraphNode) -> bool:
        if neighbor is not None and type(neighbor) is GraphNode:
            return neighbor.Value in self.Neighbors
        return False

    @classmethod
    def HasNeighbor(self, value: int) -> bool:
        if value is not None and type(value) is int:
            return value in self.Neighbors
        return False

    @classmethod
    def ClearAllNeighbors(self) -> None:
        self.Neighbors.clear()