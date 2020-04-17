using System;
public class DFSPathFinderUndirected : PathFinder
{
    public DFSPathFinderUndirected(Graph graph, int vertex) : base(graph, vertex)
    {

    }

    protected override void traverse(Graph graph, int cur_vertex)
    {
        marked[cur_vertex] = true;

        foreach (int edge in graph.getAdj()[cur_vertex])
        {
            edgeTo[edge] = cur_vertex;

            if (!marked[edge])
            {
                traverse(graph, edge);
            }
        }

    }
}