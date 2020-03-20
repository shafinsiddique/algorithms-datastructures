

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
    graph = {"A": ["B", "C", "D"],
             "B": ["A", "C"],
             "C": ['B', 'A'],
             'D': ['A']}

    print(path_exists(graph, "B","D"))