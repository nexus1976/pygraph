from enum import Enum
from graphNode import GraphNode
from typing import Dict, List

class TraversalType(Enum):
    DepthFirst = 0,
    BreadthFirst = 1

class Graph:
    def __init__(self):
        self.nodes: Dict[int, GraphNode] = {}

    @property
    def Nodes(self) -> Dict[int, GraphNode]:
        return self.nodes
    
    def AddNode(self, value: int) -> bool:
        if value is not None and type(value) is int:
            if value not in self.nodes:
                node = GraphNode(value)
                self.nodes[value] = node
                return True
        return False
    
    def RemoveNode(self, value: int) -> bool:
        if value is not None and type(value) is int:
            if value in self.nodes:
                self.nodes.pop(value)
                return True
        return False
        
    def AddEdge(self, value1: int, value2: int) -> bool:
        if value1 is None or type(value1) is not int or value2 is None or type(value2) is not int:
            return False
        if value1 not in self.nodes or value2 not in self.nodes:
            return False
        node1 = self.nodes[value1]
        node2 = self.nodes[value2]
        node1.AddNeighbor(node2)
        node2.AddNeighbor(node1)
        return True
    
    def RemoveEdge(self, value1: int, value2: int) -> bool:
        if value1 is None or type(value1) is not int or value2 is None or type(value2) is not int:
            return False
        if value1 not in self.nodes or value2 not in self.nodes:
            return False
        node1 = self.nodes[value1]
        node2 = self.nodes[value2]
        node1.RemoveNeighbor(node2)
        node2.RemoveNeighbor(node1)
        return True
        
    def PrintTraversal(self, rootValue: int, traversalType: TraversalType) -> str:
        if rootValue is None or type(rootValue) is not int or traversalType is None or type(traversalType) is not TraversalType:
            return None
        if rootValue not in self.nodes:
            return None
        rootNode = self.nodes[rootValue]
        results: List[int] = []
        
        if traversalType == TraversalType.BreadthFirst:
            print("Got breadth first")
        elif traversalType == TraversalType.DepthFirst:
            results = self.GetDepthFirst(rootNode)
        return ' '.join(str(x) for x in results)
        
    def GetDepthFirst(self, rootNode: GraphNode) -> List[int]:
        visited: List[int] = []
        valueDepths: Dict[int, int] = {
            rootNode.Value: 0
        }
        results: List[int] = []
        self.GetDepthFirstRecursive(rootNode, visited, 0, valueDepths, results)
        return results

    def GetDepthFirstRecursive(self, node: GraphNode, visited: List[int], currentDepth: int, valueDepths: Dict[int, int], results: List[int]):
        if node is None or visited is None or results is None or valueDepths is None or node.Value in visited:
            return
        results.append(node.Value)
        nextDepth: int = currentDepth + 1
        if node.Neighbors is not None and len(node.Neighbors) > 0:
            for neighbor in node.Neighbors:
                if neighbor.Value not in valueDepths.keys():
                    valueDepths[neighbor.Value] = nextDepth
                    self.GetDepthFirstRecursive(neighbor, visited, nextDepth, valueDepths, results)
        visited.append(node.Value)