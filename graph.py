from enum import Enum
from graphNode import GraphNode
from typing import Dict

class TraversalType(Enum):
    DepthFirst = 0,
    BreadthFirst = 1

class Graph:

    Nodes: Dict[int, GraphNode] = {}

    def __init__(self) -> None:
        pass
    
    @classmethod
    def AddNode(self, value: int) -> bool:
        if value is not None and type(value) is int:
            if value not in self.Nodes:
                node = GraphNode(value)
                self.Nodes[value] = node
                return True
        return False
    
    @classmethod
    def RemoveNode(self, value: int) -> bool:
        if value is not None and type(value) is int:
            if value in self.Nodes:
                self.Nodes.pop(value)
                return True
        return False
        
    @classmethod
    def AddEdge(self, value1: int, value2: int) -> bool:
        if value1 is None or type(value1) is not int or value2 is None or type(value2) is not int:
            return False
        if value1 not in self.Nodes or value2 not in self.Nodes:
            return False
        node1 = self.Nodes[value1]
        node2 = self.Nodes[value2]
        node1.AddNeighbor(node2)
        node2.AddNeighbor(node1)
        return True
    
    @classmethod
    def RemoveEdge(self, value1: int, value2: int) -> bool:
        if value1 is None or type(value1) is not int or value2 is None or type(value2) is not int:
            return False
        if value1 not in self.Nodes or value2 not in self.Nodes:
            return False
        node1 = self.Nodes[value1]
        node2 = self.Nodes[value2]
        node1.RemoveNeighbor(node2)
        node2.RemoveNeighbor(node1)
        return True
        
    #def PrintTraversal(rootValue: int, traversalType: TraversalType) -> str:
        