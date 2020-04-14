using System;
using System.Collections.Generic;

public class UndirectedGraph {
    private int vertices;
    public HashSet<int>[] adj;

    public UndirectedGraph(int numVertices) {
        this.vertices = numVertices;  
        this.adj = new HashSet<int>[vertices];

        for (int x=0; x<vertices; x++) {
            adj[x] = new HashSet<int>();
        }  

    }

    public void addEdge(int v, int w) {
        adj[v].Add(w);
        adj[w].Add(v);
    }


    
    public Boolean isAdjacent(int v, int w) {
        return this.adj[v].Contains(w);
    }

    public override String ToString() {
        String string_rep = "";

        for (int x=0; x<vertices; x++) {
            string_rep += x + ": ";

            foreach (int edge in adj[x]) {
                string_rep += edge + " ";
            }

            string_rep += "\n";
        }

        return string_rep;
    }


    public int Length() {
        return this.vertices;
    }

}

public class DepthFirstPaths {
    private Boolean[] marked;
    private int[] edgeTo;
    private int s;


    public DepthFirstPaths(UndirectedGraph graph, int vertex) {
        marked = new Boolean[graph.Length()];
        edgeTo = new int[graph.Length()];
        for (int x=0; x<graph.Length(); x++) {
            marked[x] = false;


        }

        DFS(graph, vertex);

    }

    private void DFS(UndirectedGraph graph, int v) {
        marked[v] = true;
        foreach (int edge in graph.adj[v]) {
            if (!marked[edge]) {
                edgeTo[edge] = v;
                DFS(graph, edge);
            }
        }
    }

    public Boolean hasPath(int i){
        return marked[i];
    }
}