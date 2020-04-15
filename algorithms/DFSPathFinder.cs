using System;
public class DFSPathFinder : PathFinder {

    public DFSPathFinder(Graph graph, int vertex) : base(graph, vertex) {
        
    }
    protected override void traverse(Graph graph, int vertex){
        marked[vertex] = true;

        foreach (int e in graph.getAdj()[vertex]) {
            if (!marked[e]) {
                edgeTo[e] = vertex;
                traverse(graph, e);
            }
        }
    }


    }

