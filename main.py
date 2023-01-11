from graph import Graph, TraversalType
from typing import List

def BuildGraph(nodes: List[int], edges: List[tuple]) -> Graph:
    myGraph: Graph = Graph()
    for value in nodes:
        myGraph.AddNode(value)
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        myGraph.AddEdge(node1, node2)
    return myGraph

nodes = [0, 1, 2, 3, 4, 5, 6, 7]
edges = [
    ( 0, 1 ),
    ( 0, 2 ),
    ( 0, 7 ),
    ( 1, 4 ),
    ( 2, 4 ),
    ( 2, 3 ),
    ( 3, 5 ),
    ( 3, 6 ),
    ( 7, 6 )]

myGraph = BuildGraph(nodes, edges)

depthFirstResults = myGraph.PrintTraversal(0, TraversalType.DepthFirst)
print(f'DFS: {depthFirstResults}\n')

breadthFirstResults = myGraph.PrintTraversal(0, TraversalType.BreadthFirst)
print(f'BDF: {breadthFirstResults}\n')