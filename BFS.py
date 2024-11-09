from collections import defaultdict

class BF_Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        '''Add edge from node u to node v'''
        self.graph[u].append(v)

    def traverse(self, s):
        '''Traverse the graph and print all vertices'''

        # Start by marking all vertices as unvisited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the start node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=' ')

            # Get all adjacent vertices of the dequeued vertex s
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Create a graph
g = BF_Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Breath-First Traversal (start from vertex 2):")
g.traverse(2)