public class BFSPathFinderUndirected : PathFinder
{
    public BFSPathFinderUndirected(Graph graph, int vertex) : base(graph, vertex)
    {

    }

    protected override void traverse(Graph graph, int vertex)
    {
        Queue queue = new Queue();
        queue.enqueue(vertex);

        while (!queue.isEmpty())
        {
            int cur_vertex = (int)queue.dequeue();
            marked[cur_vertex] = true;
            foreach (int edge in graph.getAdj()[cur_vertex])
            {
                if (!marked[edge])
                {
                    queue.enqueue(edge);
                    edgeTo[edge] = cur_vertex;
                }
            }
        }
    }
}