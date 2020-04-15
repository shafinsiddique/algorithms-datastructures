using System;

public class BFSPathFinder : PathFinder{
    public BFSPathFinder(Graph graph, int vertex) : base(graph, vertex) {
    }
    
    protected override void traverse(Graph graph, int vertex) {
        Queue q = new Queue();

        q.enqueue(vertex);

        while(!q.isEmpty()) {
            int cur_vertex  = (int)q.dequeue();
            marked[cur_vertex] = true;
            foreach (int edge in graph.getAdj()[cur_vertex]) {
                if (!marked[edge]) {
                    q.enqueue(edge);
                    edgeTo[edge] = cur_vertex;
                }
            }

        }
    }
}