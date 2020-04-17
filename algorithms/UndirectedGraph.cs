using System;
using System.Collections.Generic;


public class UndirectedGraph : Graph {
    private int vertices;
    public HashSet<int>[] adj;

    public UndirectedGraph(int numVertices) : base(numVertices) {

    }

    public override void addEdge(int v, int w) {
        adj[v].Add(w);
        adj[w].Add(v);
    }


}

