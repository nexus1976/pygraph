from typing import Dict, List
# from graphNode import GraphNode

class GraphNode:
    def __init__(self, value) -> None:
        self._value = value
        self._neighbors: Dict[int, GraphNode] = {}

    def __str__(self) -> str:
        strTemplate = "GraphNode Value: {0} | Neighbors Count: {1}"
        return strTemplate.format(self.Value, len(self._neighbors))
    
    @property
    def Neighbors(self) -> List['GraphNode']:
        return self._neighbors.values()
    
    @property
    def Value(self) -> int:
        return self._value

    def AddNeighbor(self, neighbor: 'GraphNode') -> bool:
        if neighbor is not None and type(neighbor) is GraphNode:
            if neighbor.Value not in self._neighbors:
                self._neighbors[neighbor.Value] = neighbor
                return True
        return False
    
    def RemoveNeighbor(self, neighbor: 'GraphNode') -> bool:
        if neighbor is not None and type(neighbor) is GraphNode:
            if neighbor.Value in self._neighbors:
                self._neighbors.pop(neighbor.Value)
                return True
        return False
    
    def RemoveNeighbor(self, value: int) -> bool:
        if value is not None and type(value) is int:
            if value in self._neighbors:
                self._neighbors.pop(value)
                return True
        return False

    def HasNeighbor(self, neighbor: 'GraphNode') -> bool:
        if neighbor is not None and type(neighbor) is GraphNode:
            return neighbor.Value in self._neighbors
        return False

    def HasNeighbor(self, value: int) -> bool:
        if value is not None and type(value) is int:
            return value in self._neighbors
        return False

    def ClearAllNeighbors(self) -> None:
        self._neighbors.clear()