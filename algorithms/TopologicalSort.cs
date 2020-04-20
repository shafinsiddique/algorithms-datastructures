using System;
using System.Collections;
public class TopologicalSort
{
    Boolean[] marked;
    LinkedStack topologicalOrder = new LinkedStack();

    public TopologicalSort(Graph graph)
    {
        marked = new Boolean[graph.Length()];

        for (int x = 0; x < marked.Length; x++)
        {
            marked[x] = false;
        }

        for (int x = 0; x < marked.Length; x++)
        {
            if (!marked[x])
            {
                DFS(graph, x);
            }
        }

    }

    public static LinkedStack sort(DirectedGraph graph) {
        TopologicalSort ts = new TopologicalSort(graph);
        return ts.getOrder();
    }
    public LinkedStack getOrder() {
        return topologicalOrder;
    }

    public void DFS(Graph graph, int vertex)
    {
        marked[vertex] = true;

        foreach (int edge in graph.getAdj()[vertex])
        {
            if (!marked[edge])
            {
                DFS(graph, edge);
            }
        }

        topologicalOrder.push(vertex);

    }


    public override String ToString()
    {
        return topologicalOrder.ToString();
    }

}