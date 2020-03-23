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
    pass