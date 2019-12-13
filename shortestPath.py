"""
Shortest Path
Have the function ShortestPath(strArr) take strArr which will be an array of strings which models a non-looping Graph. The structure of the array will be as follows: The first element in the array will be the number of nodes N (points) in the array as a string. The next N elements will be the nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.). Then after the Nth element, the rest of the elements in the array will be the connections between all of the nodes. They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.). Although, there may exist no connections at all.

An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. Your program should return the shortest path from the first Node to the last Node in the array separated by dashes. So in the example above the output should be A-B-D. Here is another example with strArr being ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]. The output for this array should be A-E-D-F-G. There will only ever be one shortest path for the array. If no path between the first and last node exists, return -1. The array will at minimum have two nodes. Also, the connection A-B for example, means that A can get to B and B can get to A.

Hard challenges are worth 15 points and you are not timed for them.
Examples
Input: ["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]
Output: A-C-D-F
Input: ["4","X","Y","Z","W","X-Y","Y-Z","X-W"]
Output: X-W
"""


class Queue():
    """
    The Queue ADT
    """

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """The Graph ADT"""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    def shortest_path(self, start, end):
        # create a queue
        q = Queue()
        # enqueue the start vertice as a list
        q.enqueue([start])
        # initialize visited as an empty set
        visited = set()
        # loop while queue is not empty
        while q.size() > 0:
            # dequeue the path
            path = q.dequeue()
            # set v to the last item in q
            v = path[-1]
            # check if v is not in visited
            if v not in visited:
                # check if v is the end
                if v == end:
                    # return the path
                    return path
                # add v to visited
                visited.add(v)
                # loop through vert connected to v
                for vert in self.vertices[v]:
                    # create a copy of the list
                    new_path = list(path)
                    # append current vet to the list
                    new_path.append(vert)
                    # enqueue the list
                    q.enqueue(new_path)
        # return -1 if shortest path not found
        return -1


def buildGraph(graph, attr):
    """
    Parses an input in this format ["4","X","Y","Z","W","X-Y","Y-Z","X-W"]
    and builds the graph from it
    """
    # get the number of vertices
    numOfVert = int(attr[0])
    # get the vertices from a range of 1 to vertices plus one
    vertices = attr[1: numOfVert + 1]

    # add all the vertices to the graph
    for vertice in vertices:
        graph.add_vertex(vertice)

    # get the edges from range of vertices plus one to the end
    edges = attr[numOfVert + 1:]

    # loop through the edges
    for edge in edges:
        # split the edge on '-'
        i, j = edge.split('-')
        # add the edge
        graph.add_edge(i, j)

    # return the vertices
    return vertices


# g = Graph()
# buildGraph(g, ["5", "A", "B", "C", "D", "F",
#                "A-B", "A-C", "B-C", "C-D", "D-F"])
# print(g.vertices)


def ShortestPath(strArr):
    # first, parse the input and represent the data like a graph
    # to find the shortest path, use bfs,
    # will have to define a queue class to use
    # find the path and join with - to match the test result.

    # create a graph object
    graph = Graph()
    # build the graph and get the vertices returned
    vertices = buildGraph(graph, strArr)
    # call the shortest path with first and last vertice
    path = graph.shortest_path(vertices[0], vertices[-1])

    return path
