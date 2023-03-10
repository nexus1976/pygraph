from enum import Enum
from graphNode import GraphNode
from typing import Dict, List

class TraversalType(Enum):
    DepthFirst = 0,
    BreadthFirst = 1

class Graph:
    def __init__(self):
        self._nodes: Dict[int, GraphNode] = {}

    @property
    def Nodes(self) -> Dict[int, GraphNode]:
        return self._nodes
    
    def AddNode(self, value: int) -> bool:
        if value is not None and type(value) is int:
            if value not in self._nodes:
                node = GraphNode(value)
                self._nodes[value] = node
                return True
        return False
    
    def RemoveNode(self, value: int) -> bool:
        if value is not None and type(value) is int:
            if value in self._nodes:
                self._nodes.pop(value)
                return True
        return False
        
    def AddEdge(self, value1: int, value2: int) -> bool:
        if value1 is None or type(value1) is not int or value2 is None or type(value2) is not int:
            return False
        if value1 not in self._nodes or value2 not in self._nodes:
            return False
        node1 = self._nodes[value1]
        node2 = self._nodes[value2]
        node1.AddNeighbor(node2)
        node2.AddNeighbor(node1)
        return True
    
    def RemoveEdge(self, value1: int, value2: int) -> bool:
        if value1 is None or type(value1) is not int or value2 is None or type(value2) is not int:
            return False
        if value1 not in self._nodes or value2 not in self._nodes:
            return False
        node1 = self._nodes[value1]
        node2 = self._nodes[value2]
        node1.RemoveNeighbor(node2)
        node2.RemoveNeighbor(node1)
        return True
        
    def PrintTraversal(self, rootValue: int, traversalType: TraversalType) -> str:
        if rootValue is None or type(rootValue) is not int or traversalType is None or type(traversalType) is not TraversalType:
            return None
        if rootValue not in self._nodes:
            return None
        rootNode = self._nodes[rootValue]
        results: List[int] = []
        
        if traversalType == TraversalType.BreadthFirst:
            results = self.GetBreadthFirst(rootNode)
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

    def GetBreadthFirst(self, rootNode: GraphNode) -> List[int]:
        results: List[int] = []
        valueDepths: Dict[int, int] = {
            rootNode.Value: 0
        }
        depthQueues: Dict[int, List[int]] = {}
        self.GetBreadthFirstRecursion(rootNode, 0, depthQueues, valueDepths)
        depthCount: int = len(depthQueues)
        for depth in range(depthCount):
            currentDepthQueue: List[int] = depthQueues[depth]
            for nodeValue in currentDepthQueue:
                results.append(nodeValue)
        return results
    
    def GetBreadthFirstRecursion(self, node: GraphNode, currentDepth: int, depthQueues: Dict[int, List[int]], valueDepths: Dict[int, int]):
        if node is None or depthQueues is None or valueDepths is None:
            return
        if currentDepth not in depthQueues:
            depthQueues[currentDepth] = []
        currentDepthQueue = depthQueues[currentDepth]
        if node.Value not in currentDepthQueue:
            currentDepthQueue.append(node.Value)
        nextDepth: int = currentDepth + 1

        if node.Neighbors is not None and len(node.Neighbors) > 0:
            for neighbor in node.Neighbors:
                if neighbor.Value not in valueDepths:
                    valueDepths[neighbor.Value] = nextDepth
            for neighbor in node.Neighbors:
                if neighbor.Value in valueDepths:
                    neighborLevel = valueDepths[neighbor.Value]
                    if neighborLevel > nextDepth:
                        valueDepths[neighbor.Value] = nextDepth
                        depthQueues[neighborLevel].remove(neighbor.Value)
                        self.GetBreadthFirstRecursion(neighbor, nextDepth, depthQueues, valueDepths)
                    elif neighborLevel == nextDepth:
                        self.GetBreadthFirstRecursion(neighbor, nextDepth, depthQueues, valueDepths)
                    