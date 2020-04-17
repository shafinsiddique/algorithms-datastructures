using System;
using System.Collections.Generic;


public class UndirectedGraph : Graph
{
    public UndirectedGraph(int numVertices) : base(numVertices)
    {

    }

    public override void addEdge(int v, int w)
    {
        adj[v].Add(w);
        adj[w].Add(v);
    }


}

