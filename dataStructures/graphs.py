class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.name] = vertex


    def add_edge(self, p1, p2):
        self.vertices[p1].neighbors.add(self.vertices[p2].name)
        self.vertices[p2].neighbors.add(self.vertices[p1].name)

    def remove_edge(self, p1, p2):
        self.vertices[p1].neighbors.remove(p2)
        self.vertices[p2].neighbors.remove(p1)

    def __str__(self):
        s = ""
        for vertex in self.vertices:
            s += "{}: {}\n".format(vertex, self.vertices[vertex].neighbors)

        return s

    def path_exists(self, v1, v2, visited=[]):
        """return true if a path exists between v1 and v2"""

        if v2 in self.vertices[v1].neighbors:
            return True

        else:
            visited.append(v1)
            for neighbor in self.vertices[v1].neighbors:
                if neighbor not in visited and self.path_exists(neighbor, v2, visited):
                    return True

            return False

def path_exists(graph, p1, p2):
    '''return true if a path exists between p1 and p2.'''

    if p2 in graph[p1]:
        return True

    else:
        for nodes in graph[p1]:
            if p2 in graph[nodes]:
                return True

        return False






if __name__ == "__main__":
    g = Graph()
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v4 = Vertex("D")

    g.add_vertex(v1)
    g.add_vertex(v2)
    g.add_vertex(v3)
    g.add_vertex(v4)
    g.add_vertex(Vertex("E"))
    g.add_edge("A","B")
    g.add_edge("B","C")
    g.add_edge("C","D")
    g.add_edge("D","E")
    print(g.path_exists("C","E"))

