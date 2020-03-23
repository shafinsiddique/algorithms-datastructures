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

def find_the_town_judge(n, trust):
    '''find the town judge.'''

    graph = {}
    # mapping people to people they trust and people they are trusted by.
    for x in range(1, n+1):
        graph[x] = [set(), set()]

    for pairs in trust:
        graph[pairs[0]][0].add(pairs[1])
        graph[pairs[1]][1].add(pairs[0])

    town_judge = None

    for people in graph:
        if len(graph[people][0]) == 0 and len(graph[people][1]) == n-1:
            if town_judge:
                return -1
            else:
                town_judge = people

    return town_judge




if __name__ == "__main__":
    # g = Graph()
    # v1 = Vertex("A")
    # v2 = Vertex("B")
    # v3 = Vertex("C")
    # v4 = Vertex("D")
    #
    # g.add_vertex(v1)
    # g.add_vertex(v2)
    # g.add_vertex(v3)
    # g.add_vertex(v4)
    # g.add_vertex(Vertex("E"))
    # g.add_edge("A","B")
    # g.add_edge("B","C")
    # g.add_edge("C","D")
    # g.add_edge("D","E")
    # print(g.path_exists("C","E"))
    print(find_the_town_judge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))

