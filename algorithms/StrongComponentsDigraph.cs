using System;
public class StrongComponents
{
    int[] ids;
    int count;
    Boolean[] marked;

    public StrongComponents(DirectedGraph graph)
    {
        ids = new int[graph.Length()];
        marked = new Boolean[graph.Length()];

        for (int x = 0; x < marked.Length; x++)
        {
            marked[x] = false;
        }

        LinkedStack elements = TopologicalSort.sort(graph);

        while (!elements.isEmpty())
        {
            int cur_vertex = (int)elements.pop();

            if (!marked[cur_vertex])
            {
                DFS(graph, cur_vertex);
                count++;
            }
        }

    }

    public Boolean isConnected(int v1, int v2)
    {
        return ids[v1] == ids[v2];
    }

    private void DFS(Graph graph, int vertex)
    {
        marked[vertex] = true;
        ids[vertex] = count;
        foreach (int edge in graph.getAdj()[vertex])
        {
            if (!marked[edge])
            {
                DFS(graph, edge);
            }
        }
    }

}